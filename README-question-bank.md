# OutSystems Question Bank Management System

OutSystems Associate Developer O11 대비 문제은행을 효율적으로 관리하는 TypeScript 기반 CLI 도구입니다.

## 📁 레포 구조

```
outsystems-certification-practice/
├── data/
│   ├── questions.jsonl         # 모든 문제 (JSONL 형식)
│   └── index.json              # 메타데이터 (topic별 개수, 마지막 ID 등)
├── scripts/
│   ├── add-question.ts         # CLI 메인 스크립트
│   ├── types.ts                # TypeScript 타입 정의
│   └── validation.ts           # 스키마 검증 유틸리티
├── tests/
│   └── add-question.test.ts    # 단위 테스트
├── exports/                    # MD/CSV 내보내기 출력 디렉토리
├── incoming/                   # 입력 파일 임시 디렉토리
├── dist/                       # 컴파일된 JavaScript 출력
├── tsconfig.json               # TypeScript 설정
├── jest.config.js              # Jest 테스트 설정
├── package.json                # Node.js 프로젝트 설정
└── README-question-bank.md     # 이 파일
```

## 🔧 설치

```bash
# 의존성 설치
npm install

# TypeScript 컴파일
npm run build
```

## 📝 데이터 포맷

문제는 `data/questions.jsonl` 파일에 JSONL 형식(한 줄에 JSON 1개)으로 저장됩니다.

### 스키마

```typescript
{
  id: string;           // 형식: OSAD-#### (예: OSAD-0001)
  topic: string;        // 예: "Client Variables", "Screen Lifecycle"
  difficulty: 1|2|3;    // 1=Easy, 2=Medium, 3=Hard
  stem: string;         // 문제 본문
  choices: [string, string, string, string]; // 정확히 4개 (A, B, C, D)
  answer: "A"|"B"|"C"|"D"; // 정답
  explanation: string;  // 해설
  tags: string[];       // 추가 태그
  source: string;       // 출처 (예: "Generated", "Official")
}
```

### 예제

```json
{
  "id": "OSAD-0001",
  "topic": "Client Variables",
  "difficulty": 2,
  "stem": "What is the scope of a Client Variable in OutSystems?",
  "choices": [
    "Available across all screens in the application",
    "Available only within the current screen",
    "Available only during the current session",
    "Available permanently on the device"
  ],
  "answer": "A",
  "explanation": "Client Variables are available across all screens in the client-side scope of the application.",
  "tags": ["variables", "client-side", "scope"],
  "source": "Generated"
}
```

## 🚀 사용법

### 문제 추가하기

```bash
# 기본 사용법
npm run add-question -- --file incoming/new_questions.json

# topic과 difficulty 기본값 지정
npm run add-question -- --file incoming/new_questions.json --topic "Client Variables" --difficulty 2

# 추가 후 Markdown으로 내보내기
npm run add-question -- --file incoming/new_questions.json --export md

# 추가 후 CSV로 내보내기
npm run add-question -- --file incoming/new_questions.json --export csv
```

### 옵션

- `-f, --file <path>`: 입력 파일 경로 (JSON 또는 JSONL 형식) **[필수]**
- `-t, --topic <topic>`: 문제에 topic이 없을 경우 기본값
- `-d, --difficulty <level>`: 문제에 difficulty가 없을 경우 기본값 (1, 2, 3)
- `-e, --export <format>`: 추가 후 내보내기 형식 (`md` 또는 `csv`)

### 입력 파일 형식

#### JSON 배열 (incoming/questions.json)

```json
[
  {
    "topic": "Client Variables",
    "difficulty": 2,
    "stem": "Question text here...",
    "choices": ["Option A", "Option B", "Option C", "Option D"],
    "answer": "A",
    "explanation": "Explanation here...",
    "tags": ["tag1", "tag2"],
    "source": "Generated"
  }
]
```

#### JSONL (incoming/questions.jsonl)

```jsonl
{"topic":"Client Variables","difficulty":2,"stem":"Question 1...","choices":["A","B","C","D"],"answer":"A","explanation":"...","tags":[],"source":"Generated"}
{"topic":"Screen Lifecycle","difficulty":3,"stem":"Question 2...","choices":["A","B","C","D"],"answer":"B","explanation":"...","tags":[],"source":"Generated"}
```

> **참고:** ID는 자동으로 발급됩니다 (OSAD-0001부터 증가). ID를 직접 지정할 수도 있지만 중복 체크가 수행됩니다.

## ✅ 검증 기능

스크립트는 다음 사항을 자동으로 검증합니다:

- ✓ ID 형식 검증 (OSAD-#### 패턴)
- ✓ 필수 필드 누락 확인
- ✓ choices 정확히 4개인지 확인
- ✓ answer가 A, B, C, D 중 하나인지 확인
- ✓ difficulty가 1, 2, 3 중 하나인지 확인
- ✓ 중복 ID 확인
- ✓ 이모지 및 특수 유니코드 문자 제거 (UTF-8 clean)

검증 실패 시 해당 문제는 추가되지 않으며, 명확한 에러 메시지가 출력됩니다.

## 📊 내보내기

### Markdown

```bash
npm run add-question -- --file incoming/questions.json --export md
```

생성 결과: `exports/questions-<timestamp>.md`

- 전체 문제 목록
- Topic별 통계
- Difficulty별 통계
- 각 문제별 상세 내용

### CSV

```bash
npm run add-question -- --file incoming/questions.json --export csv
```

생성 결과: `exports/questions-<timestamp>.csv`

- Excel/Google Sheets에서 바로 열 수 있는 형식
- 모든 필드가 컬럼으로 정리됨

## 🧪 테스트

```bash
# 모든 테스트 실행
npm test

# Watch 모드로 테스트 (개발 중)
npm run test:watch
```

### 테스트 항목 (11개)

1. ✓ 올바른 문제 검증
2. ✓ 잘못된 ID 형식 거부
3. ✓ 잘못된 choice 개수 거부
4. ✓ 잘못된 answer 거부
5. ✓ 잘못된 difficulty 거부
6. ✓ 필수 필드 누락 거부
7. ✓ ID 생성 정확성
8. ✓ 문자열 sanitization (이모지 제거)
9. ✓ 중복 ID 감지
10. ✓ JSON/JSONL 파일 파싱
11. ✓ Markdown/CSV 내보내기

## 📋 예제 워크플로우

```bash
# 1. 새 문제 파일 준비
echo '[{"topic":"RBAC","difficulty":3,"stem":"How do you...","choices":["A","B","C","D"],"answer":"A","explanation":"...","tags":[],"source":"Generated"}]' > incoming/new_q.json

# 2. 문제 추가
npm run add-question -- --file incoming/new_q.json

# 3. 전체 문제 목록 확인
npm run add-question -- --export md

# 4. 통계 확인
cat data/index.json
```

## 🛠️ 개발

### TypeScript 컴파일

```bash
npm run build
```

### 클린 빌드

```bash
npm run clean
npm run build
```

### 직접 실행 (개발 모드)

```bash
npx ts-node scripts/add-question.ts --file incoming/test.json
```

## 📌 주요 특징

- ✨ **자동 ID 발급**: 마지막 ID를 추적하여 자동 증가
- 🔍 **엄격한 검증**: 스키마 준수 여부 자동 확인
- 🧹 **문자열 정제**: 이모지 및 특수 문자 자동 제거
- 🚫 **중복 방지**: 동일 ID 추가 차단
- 📊 **통계 추적**: Topic별, Difficulty별 문제 개수 자동 업데이트
- 📤 **다양한 내보내기**: Markdown, CSV 지원
- 🧪 **테스트 커버리지**: 핵심 기능 단위 테스트 포함
- 💬 **친절한 에러 메시지**: 사람이 읽기 쉬운 검증 오류 출력

## 🐛 문제 해결

### "Cannot find module 'commander'"

```bash
npm install
```

### "TypeError: Cannot read property 'length' of undefined"

입력 파일의 JSON 형식을 확인하세요. 배열이어야 합니다.

### "Duplicate ID: OSAD-0042"

이미 존재하는 ID입니다. ID를 제거하면 자동으로 새 ID가 발급됩니다.

## 📄 라이센스

MIT

## 👤 Author

OutSystems Certification Practice Team

---

**Happy Question Banking! 🎓**
