/**
 * Question Bank Type Definitions
 * OutSystems Associate Developer O11
 */

export type Answer = "A" | "B" | "C" | "D";

export type Difficulty = 1 | 2 | 3;

export interface Question {
  id: string;               // Format: OSAD-####
  topic: string;            // e.g., "Client Variables", "Screen Lifecycle"
  difficulty: Difficulty;   // 1=Easy, 2=Medium, 3=Hard
  stem: string;             // Question text
  choices: [string, string, string, string]; // Exactly 4 choices
  answer: Answer;           // Correct answer
  explanation: string;      // Explanation of the answer
  tags: string[];           // Additional tags for categorization
  source: string;           // e.g., "Generated", "Official", "Practice"
}

export interface QuestionBankIndex {
  lastId: number;           // Last assigned ID number (e.g., 42 for OSAD-0042)
  totalQuestions: number;   // Total number of questions
  topicCounts: Record<string, number>; // Questions per topic
  difficultyCounts: Record<Difficulty, number>; // Questions per difficulty
  lastUpdated: string;      // ISO timestamp
}

export interface ValidationError {
  field: string;
  message: string;
  value?: any;
}

export interface AddQuestionOptions {
  file?: string;
  topic?: string;
  difficulty?: Difficulty;
  export?: 'md' | 'csv' | 'none';
}
