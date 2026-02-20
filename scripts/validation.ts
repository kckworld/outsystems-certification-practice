/**
 * Schema Validation Utilities
 */

import { Question, Answer, Difficulty, ValidationError } from './types';

const VALID_ANSWERS: Answer[] = ['A', 'B', 'C', 'D'];
const VALID_DIFFICULTIES: Difficulty[] = [1, 2, 3];
const ID_PATTERN = /^OSAD-\d{4}$/;

export function validateQuestion(question: any): ValidationError[] {
  const errors: ValidationError[] = [];

  // ID validation
  if (!question.id) {
    errors.push({ field: 'id', message: 'ID is required' });
  } else if (typeof question.id !== 'string') {
    errors.push({ field: 'id', message: 'ID must be a string', value: question.id });
  } else if (!ID_PATTERN.test(question.id)) {
    errors.push({ 
      field: 'id', 
      message: 'ID must follow format OSAD-#### (e.g., OSAD-0001)', 
      value: question.id 
    });
  }

  // Topic validation
  if (!question.topic) {
    errors.push({ field: 'topic', message: 'Topic is required' });
  } else if (typeof question.topic !== 'string' || question.topic.trim() === '') {
    errors.push({ field: 'topic', message: 'Topic must be a non-empty string', value: question.topic });
  }

  // Difficulty validation
  if (question.difficulty === undefined || question.difficulty === null) {
    errors.push({ field: 'difficulty', message: 'Difficulty is required' });
  } else if (!VALID_DIFFICULTIES.includes(question.difficulty)) {
    errors.push({ 
      field: 'difficulty', 
      message: 'Difficulty must be 1, 2, or 3', 
      value: question.difficulty 
    });
  }

  // Stem validation
  if (!question.stem) {
    errors.push({ field: 'stem', message: 'Question stem is required' });
  } else if (typeof question.stem !== 'string' || question.stem.trim() === '') {
    errors.push({ field: 'stem', message: 'Stem must be a non-empty string', value: question.stem });
  }

  // Choices validation
  if (!question.choices) {
    errors.push({ field: 'choices', message: 'Choices are required' });
  } else if (!Array.isArray(question.choices)) {
    errors.push({ field: 'choices', message: 'Choices must be an array', value: question.choices });
  } else if (question.choices.length !== 4) {
    errors.push({ 
      field: 'choices', 
      message: 'Exactly 4 choices required (A, B, C, D)', 
      value: `Got ${question.choices.length}` 
    });
  } else {
    // Check each choice is a non-empty string
    question.choices.forEach((choice: any, idx: number) => {
      if (typeof choice !== 'string' || choice.trim() === '') {
        errors.push({ 
          field: `choices[${idx}]`, 
          message: `Choice ${String.fromCharCode(65 + idx)} must be a non-empty string`, 
          value: choice 
        });
      }
    });
  }

  // Answer validation
  if (!question.answer) {
    errors.push({ field: 'answer', message: 'Answer is required' });
  } else if (!VALID_ANSWERS.includes(question.answer)) {
    errors.push({ 
      field: 'answer', 
      message: 'Answer must be A, B, C, or D', 
      value: question.answer 
    });
  }

  // Explanation validation
  if (!question.explanation) {
    errors.push({ field: 'explanation', message: 'Explanation is required' });
  } else if (typeof question.explanation !== 'string' || question.explanation.trim() === '') {
    errors.push({ 
      field: 'explanation', 
      message: 'Explanation must be a non-empty string', 
      value: question.explanation 
    });
  }

  // Tags validation
  if (!question.tags) {
    errors.push({ field: 'tags', message: 'Tags are required (can be empty array)' });
  } else if (!Array.isArray(question.tags)) {
    errors.push({ field: 'tags', message: 'Tags must be an array', value: question.tags });
  } else {
    question.tags.forEach((tag: any, idx: number) => {
      if (typeof tag !== 'string') {
        errors.push({ field: `tags[${idx}]`, message: 'Each tag must be a string', value: tag });
      }
    });
  }

  // Source validation
  if (!question.source) {
    errors.push({ field: 'source', message: 'Source is required' });
  } else if (typeof question.source !== 'string' || question.source.trim() === '') {
    errors.push({ field: 'source', message: 'Source must be a non-empty string', value: question.source });
  }

  return errors;
}

export function isValidQuestion(question: any): question is Question {
  return validateQuestion(question).length === 0;
}

export function sanitizeString(str: string): string {
  // Remove emojis and special unicode characters, keep only basic ASCII + common punctuation
  return str
    .replace(/[\u{1F600}-\u{1F64F}]/gu, '') // Emoticons
    .replace(/[\u{1F300}-\u{1F5FF}]/gu, '') // Misc Symbols and Pictographs
    .replace(/[\u{1F680}-\u{1F6FF}]/gu, '') // Transport and Map
    .replace(/[\u{1F1E0}-\u{1F1FF}]/gu, '') // Flags
    .replace(/[\u{2600}-\u{26FF}]/gu, '')   // Misc symbols
    .replace(/[\u{2700}-\u{27BF}]/gu, '')   // Dingbats
    .trim();
}

export function generateQuestionId(lastId: number): string {
  const nextId = lastId + 1;
  return `OSAD-${String(nextId).padStart(4, '0')}`;
}
