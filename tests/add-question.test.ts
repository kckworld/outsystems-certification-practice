/**
 * Unit Tests for Question Bank Management
 */

import * as fs from 'fs';
import * as path from 'path';
import { validateQuestion, generateQuestionId, sanitizeString, isValidQuestion } from '../scripts/validation';
import { Question, Difficulty } from '../scripts/types';
import {
  loadIndex,
  saveIndex,
  isDuplicateId,
  parseInputFile,
  addQuestionsFromFile,
  exportToMarkdown,
  exportToCSV,
} from '../scripts/add-question';

// Test data directory
const TEST_DATA_DIR = path.join(__dirname, 'test-data');
const TEST_QUESTIONS_FILE = path.join(TEST_DATA_DIR, 'test-questions.jsonl');
const TEST_INDEX_FILE = path.join(TEST_DATA_DIR, 'test-index.json');

// Setup and teardown
beforeAll(() => {
  if (!fs.existsSync(TEST_DATA_DIR)) {
    fs.mkdirSync(TEST_DATA_DIR, { recursive: true });
  }
});

afterAll(() => {
  if (fs.existsSync(TEST_DATA_DIR)) {
    fs.rmSync(TEST_DATA_DIR, { recursive: true, force: true });
  }
});

describe('Question Validation', () => {
  test('should validate a correct question', () => {
    const question: Question = {
      id: 'OSAD-0001',
      topic: 'Client Variables',
      difficulty: 2,
      stem: 'What is a client variable?',
      choices: ['A storage', 'B temporary', 'C persistent', 'D global'],
      answer: 'A',
      explanation: 'Client variables store data on the client side.',
      tags: ['basics', 'variables'],
      source: 'Generated',
    };

    const errors = validateQuestion(question);
    expect(errors).toHaveLength(0);
    expect(isValidQuestion(question)).toBe(true);
  });

  test('should reject question with invalid ID format', () => {
    const question = {
      id: 'INVALID-ID',
      topic: 'Test',
      difficulty: 1,
      stem: 'Test question',
      choices: ['A', 'B', 'C', 'D'],
      answer: 'A',
      explanation: 'Test',
      tags: [],
      source: 'Test',
    };

    const errors = validateQuestion(question);
    expect(errors.length).toBeGreaterThan(0);
    expect(errors.some(e => e.field === 'id')).toBe(true);
  });

  test('should reject question with wrong number of choices', () => {
    const question = {
      id: 'OSAD-0001',
      topic: 'Test',
      difficulty: 1,
      stem: 'Test question',
      choices: ['A', 'B', 'C'], // Only 3 choices
      answer: 'A',
      explanation: 'Test',
      tags: [],
      source: 'Test',
    };

    const errors = validateQuestion(question);
    expect(errors.some(e => e.field === 'choices')).toBe(true);
  });

  test('should reject question with invalid answer', () => {
    const question = {
      id: 'OSAD-0001',
      topic: 'Test',
      difficulty: 1,
      stem: 'Test question',
      choices: ['A', 'B', 'C', 'D'],
      answer: 'E', // Invalid answer
      explanation: 'Test',
      tags: [],
      source: 'Test',
    };

    const errors = validateQuestion(question);
    expect(errors.some(e => e.field === 'answer')).toBe(true);
  });

  test('should reject question with invalid difficulty', () => {
    const question = {
      id: 'OSAD-0001',
      topic: 'Test',
      difficulty: 5, // Invalid difficulty
      stem: 'Test question',
      choices: ['A', 'B', 'C', 'D'],
      answer: 'A',
      explanation: 'Test',
      tags: [],
      source: 'Test',
    };

    const errors = validateQuestion(question);
    expect(errors.some(e => e.field === 'difficulty')).toBe(true);
  });

  test('should reject question with missing required fields', () => {
    const question = {
      id: 'OSAD-0001',
      // Missing topic, stem, choices, etc.
    };

    const errors = validateQuestion(question);
    expect(errors.length).toBeGreaterThan(5);
  });
});

describe('ID Generation', () => {
  test('should generate correct ID format', () => {
    expect(generateQuestionId(0)).toBe('OSAD-0001');
    expect(generateQuestionId(1)).toBe('OSAD-0002');
    expect(generateQuestionId(42)).toBe('OSAD-0043');
    expect(generateQuestionId(999)).toBe('OSAD-1000');
  });

  test('should pad ID numbers correctly', () => {
    const id = generateQuestionId(5);
    expect(id).toMatch(/^OSAD-\d{4}$/);
    expect(id).toBe('OSAD-0006');
  });
});

describe('String Sanitization', () => {
  test('should remove emojis from strings', () => {
    const input = 'Hello 😀 World 🌍';
    const output = sanitizeString(input);
    expect(output).toBe('Hello  World');
  });

  test('should trim whitespace', () => {
    const input = '  Test String  ';
    const output = sanitizeString(input);
    expect(output).toBe('Test String');
  });

  test('should handle empty strings', () => {
    expect(sanitizeString('')).toBe('');
    expect(sanitizeString('   ')).toBe('');
  });
});

describe('Duplicate Detection', () => {
  test('should detect duplicate IDs', () => {
    const questions: Question[] = [
      {
        id: 'OSAD-0001',
        topic: 'Test',
        difficulty: 1,
        stem: 'Question 1',
        choices: ['A', 'B', 'C', 'D'],
        answer: 'A',
        explanation: 'Explanation',
        tags: [],
        source: 'Test',
      },
      {
        id: 'OSAD-0002',
        topic: 'Test',
        difficulty: 1,
        stem: 'Question 2',
        choices: ['A', 'B', 'C', 'D'],
        answer: 'B',
        explanation: 'Explanation',
        tags: [],
        source: 'Test',
      },
    ];

    expect(isDuplicateId('OSAD-0001', questions)).toBe(true);
    expect(isDuplicateId('OSAD-0002', questions)).toBe(true);
    expect(isDuplicateId('OSAD-0003', questions)).toBe(false);
  });
});

describe('File Parsing', () => {
  test('should parse JSON array file', () => {
    const testFile = path.join(TEST_DATA_DIR, 'test-input.json');
    const testData = [
      { id: 'OSAD-0001', topic: 'Test', difficulty: 1 },
      { id: 'OSAD-0002', topic: 'Test', difficulty: 2 },
    ];
    fs.writeFileSync(testFile, JSON.stringify(testData), 'utf-8');

    const parsed = parseInputFile(testFile);
    expect(parsed).toHaveLength(2);
    expect(parsed[0].id).toBe('OSAD-0001');
  });

  test('should parse JSONL file', () => {
    const testFile = path.join(TEST_DATA_DIR, 'test-input.jsonl');
    const line1 = JSON.stringify({ id: 'OSAD-0001', topic: 'Test' });
    const line2 = JSON.stringify({ id: 'OSAD-0002', topic: 'Test' });
    fs.writeFileSync(testFile, `${line1}\n${line2}`, 'utf-8');

    const parsed = parseInputFile(testFile);
    expect(parsed).toHaveLength(2);
    expect(parsed[1].id).toBe('OSAD-0002');
  });

  test('should throw error for non-existent file', () => {
    expect(() => parseInputFile('/non/existent/file.json')).toThrow();
  });
});

describe('Index Management', () => {
  test('should create default index if not exists', () => {
    const index = loadIndex();
    expect(index).toHaveProperty('lastId');
    expect(index).toHaveProperty('totalQuestions');
    expect(index).toHaveProperty('topicCounts');
    expect(index).toHaveProperty('difficultyCounts');
  });

  test('should update index correctly', () => {
    const index = loadIndex();
    index.lastId = 10;
    index.totalQuestions = 5;
    index.topicCounts = { 'Test Topic': 5 };
    saveIndex(index);

    const loadedIndex = loadIndex();
    expect(loadedIndex.lastId).toBe(10);
    expect(loadedIndex.totalQuestions).toBe(5);
    expect(loadedIndex.topicCounts['Test Topic']).toBe(5);
  });
});

describe('Export Functionality', () => {
  test('should export to markdown format', () => {
    const outputPath = path.join(TEST_DATA_DIR, 'export-test.md');
    const result = exportToMarkdown(outputPath);
    
    expect(fs.existsSync(result)).toBe(true);
    const content = fs.readFileSync(result, 'utf-8');
    expect(content).toContain('# OutSystems Associate Developer O11');
    expect(content).toContain('Total Questions:');
  });

  test('should export to CSV format', () => {
    const outputPath = path.join(TEST_DATA_DIR, 'export-test.csv');
    const result = exportToCSV(outputPath);
    
    expect(fs.existsSync(result)).toBe(true);
    const content = fs.readFileSync(result, 'utf-8');
    expect(content).toContain('ID,Topic,Difficulty');
  });
});
