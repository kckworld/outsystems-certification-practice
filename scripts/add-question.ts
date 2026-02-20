#!/usr/bin/env node
/**
 * CLI Tool for Managing OutSystems Question Bank
 * Add, validate, and export questions
 */

import { program } from 'commander';
import * as fs from 'fs';
import * as path from 'path';
import { Question, QuestionBankIndex, Difficulty } from './types';
import { validateQuestion, generateQuestionId, sanitizeString } from './validation';

const DATA_DIR = path.join(__dirname, '../data');
const QUESTIONS_FILE = path.join(DATA_DIR, 'questions.jsonl');
const INDEX_FILE = path.join(DATA_DIR, 'index.json');
const EXPORTS_DIR = path.join(__dirname, '../exports');

// Ensure directories exist
if (!fs.existsSync(DATA_DIR)) {
  fs.mkdirSync(DATA_DIR, { recursive: true });
}
if (!fs.existsSync(EXPORTS_DIR)) {
  fs.mkdirSync(EXPORTS_DIR, { recursive: true });
}

/**
 * Load the question bank index
 */
export function loadIndex(): QuestionBankIndex {
  if (!fs.existsSync(INDEX_FILE)) {
    const defaultIndex: QuestionBankIndex = {
      lastId: 0,
      totalQuestions: 0,
      topicCounts: {},
      difficultyCounts: { 1: 0, 2: 0, 3: 0 },
      lastUpdated: new Date().toISOString(),
    };
    saveIndex(defaultIndex);
    return defaultIndex;
  }
  const data = fs.readFileSync(INDEX_FILE, 'utf-8');
  return JSON.parse(data);
}

/**
 * Save the question bank index
 */
export function saveIndex(index: QuestionBankIndex): void {
  index.lastUpdated = new Date().toISOString();
  fs.writeFileSync(INDEX_FILE, JSON.stringify(index, null, 2), 'utf-8');
}

/**
 * Load all questions from JSONL file
 */
export function loadAllQuestions(): Question[] {
  if (!fs.existsSync(QUESTIONS_FILE)) {
    return [];
  }
  const data = fs.readFileSync(QUESTIONS_FILE, 'utf-8');
  const lines = data.split('\n').filter(line => line.trim() !== '');
  return lines.map(line => JSON.parse(line));
}

/**
 * Check if question ID already exists
 */
export function isDuplicateId(id: string, existingQuestions: Question[]): boolean {
  return existingQuestions.some(q => q.id === id);
}

/**
 * Append a question to the JSONL file
 */
export function appendQuestion(question: Question): void {
  const jsonLine = JSON.stringify(question) + '\n';
  fs.appendFileSync(QUESTIONS_FILE, jsonLine, 'utf-8');
}

/**
 * Parse input file and extract questions
 * Supports JSON array or JSONL format
 */
export function parseInputFile(filePath: string): any[] {
  if (!fs.existsSync(filePath)) {
    throw new Error(`Input file not found: ${filePath}`);
  }

  const content = fs.readFileSync(filePath, 'utf-8');
  const ext = path.extname(filePath).toLowerCase();

  try {
    if (ext === '.json') {
      const parsed = JSON.parse(content);
      return Array.isArray(parsed) ? parsed : [parsed];
    } else if (ext === '.jsonl') {
      const lines = content.split('\n').filter(line => line.trim() !== '');
      return lines.map(line => JSON.parse(line));
    } else {
      // Try JSON first, then JSONL
      try {
        const parsed = JSON.parse(content);
        return Array.isArray(parsed) ? parsed : [parsed];
      } catch {
        const lines = content.split('\n').filter(line => line.trim() !== '');
        return lines.map(line => JSON.parse(line));
      }
    }
  } catch (error) {
    throw new Error(`Failed to parse input file: ${error instanceof Error ? error.message : 'Unknown error'}`);
  }
}

/**
 * Add questions from input file
 */
export function addQuestionsFromFile(
  filePath: string,
  defaultTopic?: string,
  defaultDifficulty?: Difficulty
): { added: number; errors: Array<{ question: any; errors: string[] }> } {
  const questions = parseInputFile(filePath);
  const existingQuestions = loadAllQuestions();
  const index = loadIndex();

  const added: Question[] = [];
  const errors: Array<{ question: any; errors: string[] }> = [];

  for (let rawQuestion of questions) {
    // Apply defaults if provided
    if (defaultTopic && !rawQuestion.topic) {
      rawQuestion.topic = defaultTopic;
    }
    if (defaultDifficulty && !rawQuestion.difficulty) {
      rawQuestion.difficulty = defaultDifficulty;
    }

    // Auto-generate ID if not provided
    if (!rawQuestion.id) {
      rawQuestion.id = generateQuestionId(index.lastId);
      index.lastId++;
    }

    // Sanitize strings
    if (rawQuestion.stem) rawQuestion.stem = sanitizeString(rawQuestion.stem);
    if (rawQuestion.explanation) rawQuestion.explanation = sanitizeString(rawQuestion.explanation);
    if (rawQuestion.choices) {
      rawQuestion.choices = rawQuestion.choices.map((c: string) => sanitizeString(c));
    }
    if (rawQuestion.tags) {
      rawQuestion.tags = rawQuestion.tags.map((t: string) => sanitizeString(t));
    }

    // Validate
    const validationErrors = validateQuestion(rawQuestion);
    if (validationErrors.length > 0) {
      errors.push({
        question: rawQuestion,
        errors: validationErrors.map(e => `${e.field}: ${e.message}${e.value ? ` (got: ${JSON.stringify(e.value)})` : ''}`),
      });
      continue;
    }

    // Check for duplicates
    if (isDuplicateId(rawQuestion.id, existingQuestions) || isDuplicateId(rawQuestion.id, added)) {
      errors.push({
        question: rawQuestion,
        errors: [`Duplicate ID: ${rawQuestion.id}`],
      });
      continue;
    }

    added.push(rawQuestion as Question);
  }

  // Append all valid questions
  for (const question of added) {
    appendQuestion(question);

    // Update index
    index.totalQuestions++;
    index.topicCounts[question.topic] = (index.topicCounts[question.topic] || 0) + 1;
    index.difficultyCounts[question.difficulty]++;
  }

  saveIndex(index);

  return { added: added.length, errors };
}

/**
 * Export questions to Markdown format
 */
export function exportToMarkdown(outputPath?: string): string {
  const questions = loadAllQuestions();
  const index = loadIndex();

  let md = `# OutSystems Associate Developer O11 - Question Bank\n\n`;
  md += `**Total Questions:** ${index.totalQuestions}\n`;
  md += `**Last Updated:** ${new Date(index.lastUpdated).toLocaleString()}\n\n`;

  md += `## Questions by Topic\n\n`;
  Object.entries(index.topicCounts)
    .sort(([, a], [, b]) => b - a)
    .forEach(([topic, count]) => {
      md += `- **${topic}**: ${count} questions\n`;
    });

  md += `\n## Questions by Difficulty\n\n`;
  [1, 2, 3].forEach(diff => {
    const label = diff === 1 ? 'Easy' : diff === 2 ? 'Medium' : 'Hard';
    md += `- **${label} (${diff})**: ${index.difficultyCounts[diff as Difficulty]} questions\n`;
  });

  md += `\n---\n\n`;

  questions.forEach((q, idx) => {
    md += `## Question ${idx + 1}: ${q.id}\n\n`;
    md += `**Topic:** ${q.topic} | **Difficulty:** ${q.difficulty} | **Tags:** ${q.tags.join(', ')}\n\n`;
    md += `### ${q.stem}\n\n`;
    q.choices.forEach((choice, i) => {
      const letter = String.fromCharCode(65 + i);
      const marker = letter === q.answer ? '✓' : ' ';
      md += `${letter}. [${marker}] ${choice}\n`;
    });
    md += `\n**Answer:** ${q.answer}\n\n`;
    md += `**Explanation:** ${q.explanation}\n\n`;
    md += `**Source:** ${q.source}\n\n`;
    md += `---\n\n`;
  });

  const filename = outputPath || path.join(EXPORTS_DIR, `questions-${Date.now()}.md`);
  fs.writeFileSync(filename, md, 'utf-8');
  return filename;
}

/**
 * Export questions to CSV format
 */
export function exportToCSV(outputPath?: string): string {
  const questions = loadAllQuestions();

  const header = 'ID,Topic,Difficulty,Stem,Choice A,Choice B,Choice C,Choice D,Answer,Explanation,Tags,Source\n';
  const rows = questions.map(q => {
    const escapeCsv = (str: string) => `"${str.replace(/"/g, '""')}"`;
    return [
      q.id,
      escapeCsv(q.topic),
      q.difficulty,
      escapeCsv(q.stem),
      escapeCsv(q.choices[0]),
      escapeCsv(q.choices[1]),
      escapeCsv(q.choices[2]),
      escapeCsv(q.choices[3]),
      q.answer,
      escapeCsv(q.explanation),
      escapeCsv(q.tags.join('; ')),
      escapeCsv(q.source),
    ].join(',');
  });

  const csv = header + rows.join('\n');
  const filename = outputPath || path.join(EXPORTS_DIR, `questions-${Date.now()}.csv`);
  fs.writeFileSync(filename, csv, 'utf-8');
  return filename;
}

// CLI setup
program
  .name('add-question')
  .description('Add questions to the OutSystems question bank')
  .version('1.0.0');

program
  .option('-f, --file <path>', 'Input file containing questions (JSON or JSONL)')
  .option('-t, --topic <topic>', 'Default topic for questions missing topic')
  .option('-d, --difficulty <level>', 'Default difficulty (1, 2, or 3)', parseInt)
  .option('-e, --export <format>', 'Export format after adding (md or csv)')
  .action((options) => {
    try {
      if (!options.file) {
        console.error('❌ Error: --file option is required');
        process.exit(1);
      }

      console.log(`\n📁 Processing file: ${options.file}\n`);

      const result = addQuestionsFromFile(
        options.file,
        options.topic,
        options.difficulty as Difficulty | undefined
      );

      console.log(`✅ Successfully added ${result.added} question(s)`);

      if (result.errors.length > 0) {
        console.log(`\n⚠️  ${result.errors.length} question(s) failed validation:\n`);
        result.errors.forEach((err, idx) => {
          console.log(`  ${idx + 1}. Question ID: ${err.question.id || '(no ID)'}`);
          err.errors.forEach(e => console.log(`     - ${e}`));
          console.log();
        });
      }

      const index = loadIndex();
      console.log(`\n📊 Question Bank Summary:`);
      console.log(`   Total Questions: ${index.totalQuestions}`);
      console.log(`   Last ID: ${index.lastId}`);
      console.log(`   Topics: ${Object.keys(index.topicCounts).length}`);

      if (options.export) {
        console.log(`\n📤 Exporting to ${options.export.toUpperCase()}...`);
        let exportPath: string;
        if (options.export === 'md') {
          exportPath = exportToMarkdown();
        } else if (options.export === 'csv') {
          exportPath = exportToCSV();
        } else {
          console.error(`❌ Invalid export format: ${options.export}. Use 'md' or 'csv'.`);
          process.exit(1);
        }
        console.log(`✅ Exported to: ${exportPath}`);
      }

      console.log('\n✨ Done!\n');
    } catch (error) {
      console.error(`\n❌ Error: ${error instanceof Error ? error.message : 'Unknown error'}\n`);
      process.exit(1);
    }
  });

program.parse(process.argv);
