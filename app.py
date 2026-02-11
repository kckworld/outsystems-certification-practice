
import streamlit as st
import json
import os

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

# Image paths mapping
IMAGES = {
    "46": os.path.join(BASE_DIR, "Q46.png"),
    "52": os.path.join(BASE_DIR, "Q52.png"),
    "64": os.path.join(BASE_DIR, "Q64.png")
}

# Exam Versions Configuration
EXAM_VERSIONS = {
    "버전 1: 기본 모의고사 (KR/EN)": {
        "file": os.path.join(BASE_DIR, "structured_data.json"),
        "has_bilingual": True,
        "title": "🛡️ OutSystems Associate Certification Core Exam"
    },
    "버전 2: 신규 통합 모의고사 (70문항)": {
        "file": os.path.join(BASE_DIR, "new_exam_data.json"),
        "has_bilingual": False,
        "title": "📝 New Practice Exam (Core + Scenario)"
    },
    "버전 3: 고난도 시나리오 (100문항)": {
        "file": os.path.join(BASE_DIR, "scenario_exam_data.json"),
        "has_bilingual": False,
        "title": "🌪️ Advanced Scenario Mock Exam"
    },
    "버전 4: 샘플 시험 Set 1 (50문항)": {
        "file": os.path.join(BASE_DIR, "sample_exam_set1.json"),
        "has_bilingual": False,
        "title": "📚 Sample Exam Set 1"
    },
    "버전 5: 샘플 시험 Set 2 (50문항)": {
        "file": os.path.join(BASE_DIR, "sample_exam_set2.json"),
        "has_bilingual": False,
        "title": "📚 Sample Exam Set 2"
    },
    "버전 6: 샘플 시험 Set 3 (50문항)": {
        "file": os.path.join(BASE_DIR, "sample_exam_set3.json"),
        "has_bilingual": False,
        "title": "📚 Sample Exam Set 3"
    }
}

# Load data
@st.cache_data
def load_quiz_data(file_path):
    questions = []
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
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
questions, trans, opt_trans = load_quiz_data(selected_version["file"])

# Session State for User Answers
if 'current_version' not in st.session_state or st.session_state.current_version != selected_version_name:
    st.session_state.user_answers = {}
    st.session_state.submitted = False
    st.session_state.current_version = selected_version_name

if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Session State for Question Navigation
if 'quiz_mode' not in st.session_state:
    st.session_state.quiz_mode = "한 번에 보기"  # or "한 문제씩"
if 'current_question_idx' not in st.session_state:
    st.session_state.current_question_idx = 0
if 'checked_questions' not in st.session_state:
    st.session_state.checked_questions = {}  # Track which questions have been checked

# Sidebar Controls
st.sidebar.markdown("---")
st.sidebar.title("🎮 Quiz Control")

# Quiz Mode Selection
quiz_mode = st.sidebar.radio(
    "풀이 모드 선택:",
    ["한 번에 보기", "한 문제씩 풀기"],
    index=0 if st.session_state.quiz_mode == "한 번에 보기" else 1
)

if quiz_mode != st.session_state.quiz_mode:
    st.session_state.quiz_mode = quiz_mode
    st.session_state.current_question_idx = 0
    st.session_state.checked_questions = {}
    st.rerun()

if st.sidebar.button("Reset Quiz"):
    st.session_state.user_answers = {}
    st.session_state.submitted = False
    st.session_state.current_question_idx = 0
    st.session_state.checked_questions = {}
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
    if not st.session_state.submitted:
        # Check quiz mode
        if st.session_state.quiz_mode == "한 문제씩 풀기":
            # Single Question Mode
            idx = st.session_state.current_question_idx
            if idx >= len(questions):
                st.session_state.submitted = True
                st.rerun()
            
            q = questions[idx]
            
            # Progress indicator with navigation
            st.progress((idx + 1) / len(questions))
            
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
                st.image(IMAGES[q['id']], caption=f"Reference for Question {q['id']}", use_container_width=True)
            
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
                        st.image(IMAGES[q['id']], caption=f"Reference for Question {q['id']}", use_container_width=True)
                    
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
                    st.image(IMAGES[q['id']], use_container_width=True)

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

else:
    st.error(f"Question data not found. Please ensure '{selected_version['file']}' exists.")
