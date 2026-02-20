
import streamlit as st
import json
import os
from datetime import datetime

APP_VERSION = "v2026.02.21-2"

# Set page config with mobile optimization
st.set_page_config(
    page_title="OutSystems Certification Practice", 
    page_icon="🚀", 
    layout="wide",
    initial_sidebar_state="auto",  # Auto-collapse on mobile
    menu_items={
        'About': "OutSystems Certification Practice - Optimized for Mobile & Desktop"
    }
)

# 버전 표기 UI (상단에 한 번만)
st.markdown(f"<div style='text-align:right; font-size:0.9em; color:#888;'>버전: {APP_VERSION}</div>", unsafe_allow_html=True)

# Custom CSS for better aesthetics and mobile optimization
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    
    /* Mobile-first responsive design */
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            padding-top: 1rem !important;
        }
        
        h1 {
            font-size: 1.5rem !important;
        }
        
        h2, h3 {
            font-size: 1.2rem !important;
        }
        
        h4 {
            font-size: 1rem !important;
        }
        
        /* Make buttons full width on mobile */
        .stButton > button {
            width: 100% !important;
            padding: 0.75rem !important;
            font-size: 1rem !important;
            margin-bottom: 0.5rem !important;
        }
        
        /* Optimize radio buttons for touch */
        .stRadio [role="radiogroup"] label {
            padding: 1rem !important;
            font-size: 0.95rem !important;
            line-height: 1.5 !important;
        }
        
        /* Better spacing for form elements */
        .stRadio {
            margin-bottom: 1rem !important;
        }
        
        /* Responsive images */
        img {
            max-width: 100% !important;
            height: auto !important;
        }
        
        /* Better sidebar on mobile */
        section[data-testid="stSidebar"] {
            width: 100% !important;
        }
        
        /* Improve expander on mobile */
        .streamlit-expanderHeader {
            font-size: 0.95rem !important;
            padding: 0.75rem !important;
        }
        
        /* Better metrics display */
        [data-testid="stMetricValue"] {
            font-size: 1.2rem !important;
        }
        
        /* Progress bar visibility */
        .stProgress > div > div {
            height: 8px !important;
        }
    }
    
    /* Tablet adjustments */
    @media (min-width: 769px) and (max-width: 1024px) {
        .main .block-container {
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }
        
        .stButton > button {
            padding: 0.6rem 1.2rem !important;
        }
    }
    
    /* Touch-friendly elements */
    .stRadio [role="radiogroup"] {
        padding: 10px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .stRadio [role="radiogroup"] label {
        min-height: 44px; /* iOS recommended touch target */
        display: flex;
        align-items: center;
        cursor: pointer;
    }
    
    .question-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        border-left: 5px solid #2d3e50;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .correct-ans {
        color: #28a745;
        font-weight: bold;
    }
    
    .wrong-ans {
        color: #dc3545;
        font-weight: bold;
    }
    
    .explanation {
        background-color: #f1f3f5;
        padding: 15px;
        border-radius: 10px;
        font-style: italic;
        border-left: 3px solid #2d3e50;
    }
    
    /* Improve button visibility and touch targets */
    button {
        min-height: 44px !important;
        touch-action: manipulation;
    }
    
    /* Better text readability on mobile */
    p, li, span {
        line-height: 1.6;
        word-wrap: break-word;
    }
    
    /* Prevent horizontal scroll on mobile */
    .main, .block-container {
        overflow-x: hidden !important;
        max-width: 100vw !important;
    }
    </style>
""", unsafe_allow_html=True)

# Get base directory for proper file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WRONG_ANSWERS_FILE = os.path.join(BASE_DIR, "wrong_answers_history.json")

# Wrong Answer History Management Functions
def load_wrong_answers_history():
    """Load saved wrong answer history from JSON file"""
    if os.path.exists(WRONG_ANSWERS_FILE):
        try:
            with open(WRONG_ANSWERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_wrong_answers(date_key, questions):
    """Save wrong answers for a specific date"""
    history = load_wrong_answers_history()
    history[date_key] = questions
    with open(WRONG_ANSWERS_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def delete_wrong_answer(date_key, question_id):
    """Delete a specific question from a wrong answer set"""
    history = load_wrong_answers_history()
    if date_key in history:
        history[date_key] = [q for q in history[date_key] if q['id'] != question_id]
        if not history[date_key]:  # If empty, delete the date entry
            del history[date_key]
        with open(WRONG_ANSWERS_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
        return True
    return False

def delete_wrong_answer_set(date_key):
    """Delete entire wrong answer set for a date"""
    history = load_wrong_answers_history()
    if date_key in history:
        del history[date_key]
        with open(WRONG_ANSWERS_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
        return True
    return False

# Question Bank Management Functions
QUESTIONS_FILE = os.path.join(BASE_DIR, "data", "questions.jsonl")
INDEX_FILE = os.path.join(BASE_DIR, "data", "index.json")

def load_question_bank_index():
    """Load question bank index"""
    if os.path.exists(INDEX_FILE):
        try:
            with open(INDEX_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {
        "lastId": 0,
        "totalQuestions": 0,
        "topicCounts": {},
        "difficultyCounts": {"1": 0, "2": 0, "3": 0},
        "lastUpdated": datetime.now().isoformat()
    }

def save_question_bank_index(index):
    """Save question bank index"""
    index["lastUpdated"] = datetime.now().isoformat()
    os.makedirs(os.path.dirname(INDEX_FILE), exist_ok=True)
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

def generate_question_id(last_id):
    """Generate next question ID"""
    next_id = last_id + 1
    return f"OSAD-{str(next_id).zfill(4)}"

def validate_question(q):
    """Validate question schema"""
    errors = []
    
    # Required fields
    required = ["topic", "difficulty", "stem", "choices", "answer", "explanation", "tags", "source"]
    for field in required:
        if field not in q:
            errors.append(f"필수 필드 누락: {field}")
    
    # Difficulty validation
    if "difficulty" in q and q["difficulty"] not in [1, 2, 3]:
        errors.append(f"difficulty는 1, 2, 3 중 하나여야 합니다 (현재: {q['difficulty']})")
    
    # Choices validation
    if "choices" in q:
        if not isinstance(q["choices"], list):
            errors.append("choices는 배열이어야 합니다")
        elif len(q["choices"]) != 4:
            errors.append(f"choices는 정확히 4개여야 합니다 (현재: {len(q['choices'])}개)")
    
    # Answer validation
    if "answer" in q and q["answer"] not in ["A", "B", "C", "D"]:
        errors.append(f"answer는 A, B, C, D 중 하나여야 합니다 (현재: {q['answer']})")
    
    return errors

def add_questions_to_bank(questions_data):
    """Add questions to the question bank"""
    index = load_question_bank_index()
    added = []
    errors = []
    
    try:
        questions = json.loads(questions_data) if isinstance(questions_data, str) else questions_data
        if not isinstance(questions, list):
            questions = [questions]
        
        for q in questions:
            # Validate
            validation_errors = validate_question(q)
            if validation_errors:
                errors.append({"question": q.get("stem", "Unknown")[:50], "errors": validation_errors})
                continue
            
            # Generate ID if not present
            if "id" not in q or not q["id"]:
                q["id"] = generate_question_id(index["lastId"])
                index["lastId"] += 1
            
            # Append to JSONL file
            os.makedirs(os.path.dirname(QUESTIONS_FILE), exist_ok=True)
            with open(QUESTIONS_FILE, "a", encoding="utf-8") as f:
                f.write(json.dumps(q, ensure_ascii=False) + "\n")
            
            # Update index
            index["totalQuestions"] += 1
            topic = q["topic"]
            index["topicCounts"][topic] = index["topicCounts"].get(topic, 0) + 1
            difficulty = str(q["difficulty"])
            index["difficultyCounts"][difficulty] = index["difficultyCounts"].get(difficulty, 0) + 1
            
            added.append(q["id"])
        
        save_question_bank_index(index)
        return {"success": True, "added": len(added), "errors": errors, "index": index}
    
    except json.JSONDecodeError as e:
        return {"success": False, "added": 0, "errors": [{"question": "JSON 파싱 오류", "errors": [str(e)]}], "index": index}
    except Exception as e:
        return {"success": False, "added": 0, "errors": [{"question": "처리 오류", "errors": [str(e)]}], "index": index}

# Image paths mapping
IMAGES = {
    "46": os.path.join(BASE_DIR, "Q46.png"),
    "52": os.path.join(BASE_DIR, "Q52.png"),
    "64": os.path.join(BASE_DIR, "Q64.png")
}

# Exam Versions Configuration
EXAM_VERSIONS = {
    "🏦 문제은행 (Question Bank)": {
        "file": os.path.join(BASE_DIR, "data", "questions.jsonl"),
        "has_bilingual": False,
        "title": "🏦 Question Bank - Custom Questions",
        "is_jsonl": True
    },
    "버전 1: 기본 모의고사 (KR/EN)": {
        "file": os.path.join(BASE_DIR, "structured_data.json"),
        "has_bilingual": True,
        "title": "🛡️ OutSystems Associate Certification Core Exam",
        "is_jsonl": False
    },
    "버전 2: 신규 통합 모의고사 (70문항)": {
        "file": os.path.join(BASE_DIR, "new_exam_data.json"),
        "has_bilingual": False,
        "title": "📝 New Practice Exam (Core + Scenario)",
        "is_jsonl": False
    },
    "버전 3: 고난도 시나리오 (100문항)": {
        "file": os.path.join(BASE_DIR, "scenario_exam_data.json"),
        "has_bilingual": False,
        "title": "🌪️ Advanced Scenario Mock Exam",
        "is_jsonl": False
    },
    "버전 4: 샘플 시험 Set 1 (50문항)": {
        "file": os.path.join(BASE_DIR, "sample_exam_set1.json"),
        "has_bilingual": False,
        "title": "📚 Sample Exam Set 1",
        "is_jsonl": False
    },
    "버전 5: 샘플 시험 Set 2 (50문항)": {
        "file": os.path.join(BASE_DIR, "sample_exam_set2.json"),
        "has_bilingual": False,
        "title": "📚 Sample Exam Set 2",
        "is_jsonl": False
    },
    "버전 6: 샘플 시험 Set 3 (50문항)": {
        "file": os.path.join(BASE_DIR, "sample_exam_set3.json"),
        "has_bilingual": False,
        "title": "📚 Sample Exam Set 3",
        "is_jsonl": False
    }
}

# Load data
@st.cache_data
def load_quiz_data(file_path, is_jsonl=False):
    questions = []
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            if is_jsonl:
                # Read JSONL format (one JSON per line)
                for line in f:
                    line = line.strip()
                    if line:
                        questions.append(json.loads(line))
            else:
                # Read regular JSON format
                questions = json.load(f)
            
    translations = {}
    opt_translations = {}
    if "structured_data.json" in file_path:
        trans_file = os.path.join(BASE_DIR, "translations.json")
        if os.path.exists(trans_file):
            with open(trans_file, "r", encoding="utf-8") as f:
                t_data = json.load(f)
                translations = t_data.get('translations', {})
                opt_translations = t_data.get('option_translations', {})
            
    return questions, translations, opt_translations

# Sidebar for Version Selection
st.sidebar.title("📚 Exam Selection")
selected_version_name = st.sidebar.selectbox("시험 버전을 선택하세요:", list(EXAM_VERSIONS.keys()))
selected_version = EXAM_VERSIONS[selected_version_name]

# Load specific data
is_jsonl = selected_version.get("is_jsonl", False)
questions, trans, opt_trans = load_quiz_data(selected_version["file"], is_jsonl)

# Session State for User Answers
if 'current_version' not in st.session_state or st.session_state.current_version != selected_version_name:
    st.session_state.user_answers = {}
    st.session_state.submitted = False
    st.session_state.current_version = selected_version_name

if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'submitted' not in st.session_state or st.session_state.submitted not in [True, False]:
    st.session_state.submitted = False

# Session State for Question Navigation
if 'quiz_mode' not in st.session_state:
    st.session_state.quiz_mode = "한 번에 보기"  # or "한 문제씩"
if 'current_question_idx' not in st.session_state:
    st.session_state.current_question_idx = 0
if 'checked_questions' not in st.session_state:
    st.session_state.checked_questions = {}  # Track which questions have been checked

# Session State for Wrong Answer Practice
if 'user_answers_wrong' not in st.session_state:
    st.session_state.user_answers_wrong = {}
if 'checked_wrong' not in st.session_state:
    st.session_state.checked_wrong = {}
if 'current_wrong_idx' not in st.session_state:
    st.session_state.current_wrong_idx = 0
if 'submitted_wrong' not in st.session_state:
    st.session_state.submitted_wrong = False
if 'wrong_questions' not in st.session_state:
    st.session_state.wrong_questions = []
if 'wrong_answer_date_key' not in st.session_state:
    st.session_state.wrong_answer_date_key = None

# Sidebar Controls
st.sidebar.markdown("---")
st.sidebar.title("🎮 Quiz Control")

# Show current mode if in wrong answer practice
if st.session_state.quiz_mode == "오답 다시 풀기":
    st.sidebar.info("📌 현재 오답 다시 풀기 모드")

# Saved Wrong Answers Section
st.sidebar.markdown("---")
st.sidebar.subheader("💾 저장된 오답")
wrong_history = load_wrong_answers_history()
if wrong_history:
    saved_dates = list(wrong_history.keys())
    saved_dates.sort(reverse=True)
    selected_date = st.sidebar.selectbox(
        "오답 세트 선택:",
        ["-- 선택하세요 --"] + saved_dates,
        key="saved_wrong_selector"
    )
    if selected_date != "-- 선택하세요 --":
        if st.sidebar.button("이 오답 세트 불러오기"):
            st.session_state.quiz_mode = "오답 다시 풀기"
            st.session_state.wrong_questions = wrong_history[selected_date]
            st.session_state.wrong_answer_date_key = selected_date
            st.session_state.user_answers_wrong = {}
            st.session_state.current_wrong_idx = 0
            st.session_state.checked_wrong = {}
            st.session_state.submitted_wrong = False
            st.rerun()
else:
    st.sidebar.caption("저장된 오답이 없습니다.")

# Question Bank Admin Section
st.sidebar.markdown("---")
st.sidebar.subheader("🔧 문제은행 관리")

with st.sidebar.expander("📤 문제 추가하기"):
    uploaded_file = st.file_uploader(
        "JSON 파일 업로드",
        type=["json"],
        help="문제가 담긴 JSON 배열 파일을 업로드하세요",
        key="question_uploader"
    )
    
    if uploaded_file is not None:
        try:
            # Read file content
            file_content = uploaded_file.read().decode("utf-8")
            
            # Preview
            st.text_area("파일 미리보기", file_content[:500] + "...", height=100, disabled=True)
            
            # Add button
            if st.button("문제 추가하기", key="add_questions_btn"):
                with st.spinner("문제를 추가하는 중..."):
                    result = add_questions_to_bank(file_content)
                    
                    if result["success"]:
                        # Clear cache to reload questions
                        load_quiz_data.clear()
                        
                        st.success(f"✅ {result['added']}개 문제가 추가되었습니다!")
                        
                        # Show index info
                        index = result["index"]
                        st.info(f"""
**문제은행 현황**
- 전체 문제: {index['totalQuestions']}개
- 마지막 ID: {index['lastId']}
- Topic 수: {len(index['topicCounts'])}개
                        """)
                        
                        if result["errors"]:
                            st.warning(f"⚠️ {len(result['errors'])}개 문제 추가 실패")
                            with st.expander("오류 내역 보기"):
                                for err in result["errors"]:
                                    st.write(f"**문제:** {err['question']}")
                                    for e in err["errors"]:
                                        st.write(f"  - {e}")
                        
                        # Show reload button
                        st.info("💡 새로 추가된 문제를 보려면 '🏦 문제은행'을 선택하세요!")
                    else:
                        st.error("❌ 문제 추가 실패")
                        if result["errors"]:
                            for err in result["errors"]:
                                st.write(f"**{err['question']}**")
                                for e in err["errors"]:
                                    st.write(f"  - {e}")
        except Exception as e:
            st.error(f"파일 처리 오류: {str(e)}")
    
    # Show current stats
    index = load_question_bank_index()
    if index["totalQuestions"] > 0:
        st.markdown("---")
        st.markdown("**현재 문제은행**")
        st.write(f"📊 전체: {index['totalQuestions']}문제")
        st.write(f"🆔 마지막 ID: OSAD-{str(index['lastId']).zfill(4)}")

# Quiz Mode Selection
quiz_mode = st.sidebar.radio(
    "풀이 모드 선택:",
    ["한 번에 보기", "한 문제씩 풀기"],
    index=0 if st.session_state.quiz_mode in ["한 번에 보기", "오답 다시 풀기"] else 1
)

# Only update quiz_mode from sidebar if not in wrong answer practice mode
if quiz_mode != st.session_state.quiz_mode and st.session_state.quiz_mode != "오답 다시 풀기":
    st.session_state.quiz_mode = quiz_mode
    st.session_state.current_question_idx = 0
    st.session_state.checked_questions = {}
    st.rerun()

if st.sidebar.button("Reset Quiz"):
    st.session_state.user_answers = {}
    st.session_state.submitted = False
    st.session_state.current_question_idx = 0
    st.session_state.checked_questions = {}
    st.session_state.quiz_mode = "한 번에 보기"
    st.session_state.user_answers_wrong = {}
    st.session_state.checked_wrong = {}
    st.session_state.current_wrong_idx = 0
    st.session_state.submitted_wrong = False
    st.session_state.wrong_questions = []
    st.rerun()

st.title(f"{selected_version['title']}")
st.info(f"선택된 모의고사: {selected_version_name}")
st.write("---")

def get_bilingual_q(q_text):
    if not selected_version["has_bilingual"]:
        return q_text
    t = trans.get(q_text, "")
    return f"{q_text} ({t})" if t else q_text

def get_bilingual_opt(opt_text):
    if not selected_version["has_bilingual"]:
        return opt_text
    t = opt_trans.get(opt_text, "")
    return f"{opt_text} ({t})" if t else opt_text

if questions:
    # 오답만 다시 풀기 모드
    if st.session_state.quiz_mode == "오답 다시 풀기":
        wrong_questions = st.session_state.get("wrong_questions", [])
        if not wrong_questions:
            st.error("오답 데이터가 없습니다. 전체 퀴즈를 먼저 풀어주세요.")
        elif st.session_state.get("submitted_wrong", False):
            # 오답 풀이 결과
            score = 0
            for q in wrong_questions:
                if st.session_state.user_answers_wrong.get(q['id']) == q['answer_code']:
                    score += 1
            st.header("📊 오답 풀이 결과")
            st.metric("오답 문제 수", len(wrong_questions))
            st.metric("맞춘 오답 수", score, f"{score/len(wrong_questions)*100:.1f}%")
            st.progress(score / len(wrong_questions))
            if score == len(wrong_questions):
                st.success("모든 오답을 맞췄습니다! 🎉")
            else:
                st.info("아직 틀린 문제가 있습니다. 반복해서 연습하세요!")
            if st.button("🔄 오답 다시 풀기 반복"):
                st.session_state.submitted_wrong = False
                st.session_state.user_answers_wrong = {}
                st.session_state.current_wrong_idx = 0
                st.session_state.checked_wrong = {}
                st.rerun()
            if st.session_state.wrong_answer_date_key:
                if st.button("🗑️ 이 오답 세트 삭제"):
                    if delete_wrong_answer_set(st.session_state.wrong_answer_date_key):
                        st.success("오답 세트가 삭제되었습니다!")
                        st.session_state.quiz_mode = "한 번에 보기"
                        st.session_state.wrong_answer_date_key = None
                        st.rerun()
            if st.button("🏠 전체 시험으로 돌아가기"):
                st.session_state.quiz_mode = "한 번에 보기"
                st.session_state.submitted = False
                st.session_state.user_answers = {}
                st.session_state.current_question_idx = 0
                st.session_state.checked_questions = {}
                st.session_state.wrong_answer_date_key = None
                st.rerun()
        else:
            # 오답 문제 풀이
            idx = st.session_state.get("current_wrong_idx", 0)
            if idx >= len(wrong_questions):
                st.session_state.submitted_wrong = True
                st.rerun()
            q = wrong_questions[idx]
            st.markdown(f"### 오답 다시 풀기 - 문제 {q['id']}")
            st.markdown(f"#### {get_bilingual_q(q['question'])}")
            options_list = [f"{opt['code']}. {get_bilingual_opt(opt['text'])}" for opt in q['options']]
            selected = st.radio(
                f"답을 선택하세요:",
                options_list,
                index=None if q['id'] not in st.session_state.user_answers_wrong else 
                      [opt['code'] for opt in q['options']].index(st.session_state.user_answers_wrong[q['id']]) if st.session_state.user_answers_wrong.get(q['id']) else None,
                key=f"wrong_q_{idx}_{q['id']}"
            )
            if selected:
                st.session_state.user_answers_wrong[q['id']] = selected[0]
            st.write("---")
            is_checked = st.session_state.checked_wrong.get(q['id'], False)
            if not is_checked:
                if st.button("✅ 정답 확인 (오답)", use_container_width=True, type="primary"):
                    if selected:
                        st.session_state.checked_wrong[q['id']] = True
                        st.rerun()
                    else:
                        st.warning("⚠️ 답을 먼저 선택해주세요!")
            if is_checked:
                user_choice = st.session_state.user_answers_wrong.get(q['id'])
                correct_choice = q['answer_code']
                is_correct = user_choice == correct_choice
                if is_correct:
                    st.success("🎉 정답입니다!")
                else:
                    st.error(f"❌ 오답입니다. 정답은 {correct_choice}입니다.")
                st.write("---")
                st.markdown("### 📝 선택지 및 해설")
                for opt in q['options']:
                    if opt['code'] == correct_choice:
                        st.markdown(f"✅ **{opt['code']}. {get_bilingual_opt(opt['text'])}** ← 정답")
                    elif opt['code'] == user_choice and not is_correct:
                        st.markdown(f"❌ {opt['code']}. {get_bilingual_opt(opt['text'])} ← 내가 선택한 답")
                    else:
                        st.markdown(f"   {opt['code']}. {get_bilingual_opt(opt['text'])}")
                st.write("---")
                st.markdown("### 💡 해설")
                st.info(q['explanation'])
                st.write("---")
                
                # Button to mark question as mastered and remove it
                if st.session_state.wrong_answer_date_key:
                    if st.button("✅ 완벽히 이해함 (이 문제 삭제)", key=f"master_{q['id']}"):
                        if delete_wrong_answer(st.session_state.wrong_answer_date_key, q['id']):
                            # Update current wrong_questions list
                            st.session_state.wrong_questions = [wq for wq in wrong_questions if wq['id'] != q['id']]
                            if not st.session_state.wrong_questions:
                                st.success("모든 문제를 마스터했습니다! 🎉")
                                st.session_state.quiz_mode = "한 번에 보기"
                                st.session_state.wrong_answer_date_key = None
                            else:
                                st.success("문제가 삭제되었습니다!")
                                if idx >= len(st.session_state.wrong_questions):
                                    st.session_state.current_wrong_idx = len(st.session_state.wrong_questions) - 1
                            st.rerun()
                
                st.write("---")
                col1, col2 = st.columns([1, 1], gap="small")
                with col1:
                    if idx > 0:
                        if st.button("⬅️ 이전 오답", use_container_width=True):
                            st.session_state.current_wrong_idx -= 1
                            st.rerun()
                with col2:
                    if idx < len(wrong_questions) - 1:
                        if st.button("다음 오답 ➡️", use_container_width=True):
                            st.session_state.current_wrong_idx += 1
                            st.rerun()
                    else:
                        if st.button("📊 오답 풀이 결과 보기", use_container_width=True, type="primary"):
                            st.session_state.submitted_wrong = True
                            st.rerun()
            st.write("---")
            answered_count = len([a for a in st.session_state.user_answers_wrong.values() if a])
            checked_count = len([v for v in st.session_state.checked_wrong.values() if v])
            st.caption(f"📌 오답 답변: {answered_count} / {len(wrong_questions)} | 확인: {checked_count} / {len(wrong_questions)}")
    # 기존 전체/한 문제씩 모드
    elif not st.session_state.submitted:
        # Check quiz mode
        if st.session_state.quiz_mode == "한 문제씩 풀기":
            # Single Question Mode
            idx = st.session_state.current_question_idx
            if idx >= len(questions):
                st.session_state.submitted = True
                st.rerun()
            
            q = questions[idx]
            
            # Question navigator
            col1, col2 = st.columns([3, 1])
            with col1:
                selected_q = st.slider(
                    "문제 선택:",
                    min_value=1,
                    max_value=len(questions),
                    value=idx + 1,
                    key=f"question_slider_{idx}",
                    help="슬라이더를 움직여 원하는 문제로 바로 이동하세요"
                )
                if selected_q != idx + 1:
                    st.session_state.current_question_idx = selected_q - 1
                    st.rerun()
            
            with col2:
                # Quick jump input
                jump_to = st.number_input(
                    "바로가기:",
                    min_value=1,
                    max_value=len(questions),
                    value=idx + 1,
                    step=1,
                    key=f"jump_input_{idx}",
                    help="문제 번호를 입력하세요"
                )
                if jump_to != idx + 1:
                    st.session_state.current_question_idx = jump_to - 1
                    st.rerun()
            
            st.markdown(f"### 문제 {q['id']}")
            st.markdown(f"#### {get_bilingual_q(q['question'])}")
            # Show image if exists
            if q['id'] in IMAGES and selected_version["has_bilingual"] and os.path.exists(IMAGES[q['id']]):
                st.image(IMAGES[q['id']], caption=f"Reference for Question {q['id']}", width="stretch")
            
            # Format options for display
            options_list = [f"{opt['code']}. {get_bilingual_opt(opt['text'])}" for opt in q['options']]
            
            selected = st.radio(
                f"답을 선택하세요:",
                options_list,
                index=None if q['id'] not in st.session_state.user_answers else 
                      [opt['code'] for opt in q['options']].index(st.session_state.user_answers[q['id']]) if st.session_state.user_answers.get(q['id']) else None,
                key=f"single_q_{idx}_{q['id']}"
            )
            
            # Store answer
            if selected:
                st.session_state.user_answers[q['id']] = selected[0]
            
            st.write("---")
            
            # Check if this question has been checked
            is_checked = st.session_state.checked_questions.get(q['id'], False)
            
            if not is_checked:
                # Show check answer button
                if st.button("✅ 정답 확인", use_container_width=True, type="primary"):
                    if selected:
                        st.session_state.checked_questions[q['id']] = True
                        st.rerun()
                    else:
                        st.warning("⚠️ 답을 먼저 선택해주세요!")
            
            # Show answer and explanation if checked
            if is_checked:
                user_choice = st.session_state.user_answers.get(q['id'])
                correct_choice = q['answer_code']
                is_correct = user_choice == correct_choice
                
                if is_correct:
                    st.success("🎉 정답입니다!")
                else:
                    st.error(f"❌ 오답입니다. 정답은 {correct_choice}입니다.")
                
                st.write("---")
                st.markdown("### 📝 선택지 및 해설")
                
                # Display options with correct/wrong indicators
                for opt in q['options']:
                    if opt['code'] == correct_choice:
                        st.markdown(f"✅ **{opt['code']}. {get_bilingual_opt(opt['text'])}** ← 정답")
                    elif opt['code'] == user_choice and not is_correct:
                        st.markdown(f"❌ {opt['code']}. {get_bilingual_opt(opt['text'])} ← 내가 선택한 답")
                    else:
                        st.markdown(f"   {opt['code']}. {get_bilingual_opt(opt['text'])}")
                
                st.write("---")
                st.markdown("### 💡 해설")
                st.info(q['explanation'])
                
                # Navigation buttons
                st.write("---")
                # Responsive button layout
                col1, col2 = st.columns([1, 1], gap="small")
                
                with col1:
                    if idx > 0:
                        if st.button("⬅️ 이전 문제", use_container_width=True):
                            st.session_state.current_question_idx -= 1
                            st.rerun()
                
                with col2:
                    if idx < len(questions) - 1:
                        if st.button("다음 문제 ➡️", use_container_width=True):
                            st.session_state.current_question_idx += 1
                            st.rerun()
                    else:
                        if st.button("📊 전체 결과 보기", use_container_width=True, type="primary"):
                            st.session_state.submitted = True
                            st.rerun()
                
                # Copyable text section for GPT
                st.write("---")
                with st.expander("📋 복사용 텍스트 (GPT 추가 설명 요청용)", expanded=False):
                    # Build copyable text
                    copy_text = f"""문제 {q['id']}:
{get_bilingual_q(q['question'])}

선택지:
"""
                    for opt in q['options']:
                        copy_text += f"{opt['code']}. {get_bilingual_opt(opt['text'])}\n"
                    
                    copy_text += f"\n정답: {correct_choice}\n"
                    copy_text += f"내 답: {user_choice}\n"
                    copy_text += f"\n해설:\n{q['explanation']}\n"
                    copy_text += f"\n위 문제와 해설에 대해 더 자세히 설명해주세요."
                    
                    st.code(copy_text, language=None)
                    st.caption("💡 위 텍스트를 선택하여 복사한 후 ChatGPT에 붙여넣으세요.")
            
            # Show answer status
            st.write("---")
            answered_count = len([a for a in st.session_state.user_answers.values() if a])
            checked_count = len([v for v in st.session_state.checked_questions.values() if v])
            st.caption(f"📌 답변한 문제: {answered_count} / {len(questions)} | 확인한 문제: {checked_count} / {len(questions)}")
        
        else:
            # All Questions Mode (Original)
            with st.form("quiz_form"):
                for idx, q in enumerate(questions):
                    st.markdown(f"#### 문제 {q['id']}")
                    st.markdown(get_bilingual_q(q['question']))
                    
                    # Show image if exists (only for version 1 usually, but generic-safe)
                    if q['id'] in IMAGES and selected_version["has_bilingual"] and os.path.exists(IMAGES[q['id']]):
                        st.image(IMAGES[q['id']], caption=f"Reference for Question {q['id']}", width="stretch")
                    
                    # Format options for display
                    options_list = [f"{opt['code']}. {get_bilingual_opt(opt['text'])}" for opt in q['options']]
                    
                    selected = st.radio(
                        f"Select your answer for Question {q['id']}:",
                        options_list,
                        index=None,
                        key=f"q_{idx}_{q['id']}",
                        label_visibility="collapsed"
                    )
                    
                    # Store answer (just the code A, B, C...)
                    st.session_state.user_answers[q['id']] = selected[0] if selected else None
                    st.write("") # Spacer

                submit_btn = st.form_submit_button("Submit Exam / 답안 제출", use_container_width=True)
                if submit_btn:
                    st.session_state.submitted = True
                    st.rerun()
    else:
        # Results Section
        score = 0
        wrong_questions = []
        
        for q in questions:
            if st.session_state.user_answers.get(q['id']) == q['answer_code']:
                score += 1
            else:
                wrong_questions.append(q)
        
        # summary
        st.header("📊 Exam Results / 시험 결과")
        # Responsive column layout for mobile
        col1, col2, col3 = st.columns([1, 1, 1])
        col1.metric("Total Questions", len(questions))
        col2.metric("Correct Answers", score, f"{score/len(questions)*100:.1f}%")
        col3.metric("Wrong Answers", len(wrong_questions))
        
        progress = score / len(questions)
        st.progress(progress)
        
        if progress >= 0.7:
            st.success("🎉 Congratulations! You passed. (합격점 70% 이상)")
        else:
            st.error("📉 You need more practice. (합격기준 미달)")
            
        st.write("---")
        st.subheader("📝 Review & Explanations / 오답 노트 및 해설")
        
        for q in questions:
            user_choice = st.session_state.user_answers.get(q['id'], "No Answer")
            correct_choice = q['answer_code']
            is_correct = user_choice == correct_choice
            
            with st.expander(f"문제 {q['id']}: {'✅ Correct' if is_correct else '❌ Incorrect'}", expanded=True):
                st.markdown(f"**Question:** {get_bilingual_q(q['question'])}")
                
                # Show image if exists
                if q['id'] in IMAGES and selected_version["has_bilingual"] and os.path.exists(IMAGES[q['id']]):
                    st.image(IMAGES[q['id']], width="stretch")

                # Display options
                for opt in q['options']:
                    color = "black"
                    prefix = ""
                    if opt['code'] == correct_choice:
                        color = "green"
                        prefix = "✔️ **(Answer)** "
                    elif opt['code'] == user_choice and not is_correct:
                        color = "red"
                        prefix = "✖️ **(Your Choice)** "
                    
                    st.markdown(f"<p style='color:{color}; margin-left: 20px;'>{prefix}{opt['code']}. {get_bilingual_opt(opt['text'])}</p>", unsafe_allow_html=True)
                
                if not is_correct:
                    st.markdown(f"**Your Answer:** <span class='wrong-ans'>{user_choice}</span>", unsafe_allow_html=True)
                    st.markdown(f"**Correct Answer:** <span class='correct-ans'>{correct_choice}</span>", unsafe_allow_html=True)
                
                st.markdown("**Explanation / 해설:**")
                st.info(q['explanation'])
        
        if st.button("Restart Quiz / 다시 풀기"):
            st.session_state.submitted = False
            st.session_state.user_answers = {}
            st.session_state.current_question_idx = 0
            st.session_state.checked_questions = {}
            st.rerun()

        # 오답 저장 및 다시 풀기 버튼
        btn_disabled = len(wrong_questions) == 0
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("💾 오답 저장하기", disabled=btn_disabled):
                date_key = datetime.now().strftime("%Y-%m-%d %H:%M")
                save_wrong_answers(date_key, wrong_questions)
                st.success(f"✅ 오답 {len(wrong_questions)}문제가 저장되었습니다!")
                st.rerun()
        with col2:
            if st.button("❗ 오답만 다시 풀기", disabled=btn_disabled):
                st.session_state.quiz_mode = "오답 다시 풀기"
                st.session_state.wrong_questions = wrong_questions
                st.session_state.wrong_answer_date_key = None  # New practice, not from saved
                st.session_state.user_answers_wrong = {}
                st.session_state.current_wrong_idx = 0
                st.session_state.checked_wrong = {}
                st.session_state.submitted_wrong = False
                st.rerun()

else:
    # No questions available
    if "문제은행" in selected_version_name or "Question Bank" in selected_version_name:
        st.warning("📭 문제은행이 비어있습니다!")
        st.info("""
**문제 추가 방법:**
1. 사이드바에서 **🔧 문제은행 관리** 섹션 열기
2. **📤 문제 추가하기** 클릭
3. JSON 파일 업로드
4. 문제 추가 후 자동으로 반영됩니다!

**JSON 파일 형식 예시:**
```json
[
  {
    "topic": "Client Variables",
    "difficulty": 2,
    "stem": "문제 내용",
    "choices": ["A", "B", "C", "D"],
    "answer": "A",
    "explanation": "해설",
    "tags": ["tag1"],
    "source": "Generated"
  }
]
```
        """)
    else:
        st.error(f"Question data not found. Please ensure '{selected_version['file']}' exists.")
