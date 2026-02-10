# OutSystems Certification Practice Exam

🚀 OutSystems 자격증 시험 대비 연습 프로그램

## 📖 소개

OutSystems 자격증 시험을 준비하는 분들을 위한 인터랙티브 연습 문제 앱입니다. Streamlit으로 구현되어 있으며, 실시간으로 답안을 확인하고 설명을 볼 수 있습니다.

## ✨ 주요 기능

- 📝 **시험 문제 풀기**: 실제 시험과 유사한 형식의 연습 문제
- ✅ **실시간 채점**: 답안 제출 즉시 정답 확인
- 💡 **상세한 설명**: 각 문제에 대한 자세한 해설 제공
- 🖼️ **이미지 지원**: 문제에 필요한 다이어그램 및 스크린샷 포함
- 🌐 **다국어 지원**: 한국어/영어 문제 제공

## 🚀 실행 방법

### 1. 필수 패키지 설치

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 2. 앱 실행

\`\`\`bash
streamlit run app.py
\`\`\`

### 3. 브라우저에서 접속

자동으로 브라우저가 열리며, `http://localhost:8501`에서 앱을 사용할 수 있습니다.

## 📁 파일 구조

- `app.py` - 메인 Streamlit 애플리케이션
- `new_exam_data.json` - 일반 시험 문제 데이터
- `scenario_exam_data.json` - 시나리오 기반 문제 데이터
- `requirements.txt` - 필요한 Python 패키지 목록
- `Q46.png`, `Q52.png`, `Q64.png` - 문제 이미지 파일

## 📚 데이터 파일

- **Certification_EN.md** / **Certification_KR.md**: 원본 시험 문제 (영어/한국어)
- **structured_data.json**: 구조화된 문제 데이터
- **translations.json**: 번역 데이터

## 🛠️ 기술 스택

- **Python 3.11+**
- **Streamlit** - 웹 UI 프레임워크
- **JSON** - 데이터 저장 형식

## 📝 사용 방법

1. 앱 실행 후 좌측 사이드바에서 문제 번호 선택
2. 문제를 읽고 답안 선택
3. "제출" 버튼 클릭
4. 정답 여부 확인 및 해설 읽기
5. "다음 문제" 버튼으로 다음 문제로 이동

## 📄 라이센스

이 프로젝트는 학습 목적으로 제작되었습니다.

## 🤝 기여

개선 사항이나 버그 리포트는 이슈로 등록해 주세요.

---

**Happy Learning! 📚✨**
