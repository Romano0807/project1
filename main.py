import streamlit as st
import random
import time

# --- 원소 데이터베이스
elements = [
    {"name": "수소", "symbol": "H", "description": "가장 가벼운 원소이며, 우주에서 가장 풍부하게 존재"},
    {"name": "헬륨", "symbol": "He", "description": "무색, 무취의 기체로 풍선에 사용되며 불이 붙지 않음"},
    {"name": "리튬", "symbol": "Li", "description": "가장 가벼운 금속이며, 건전지에 사용"},
    {"name": "베릴륨", "symbol": "Be", "description": "항공재료에 사용되는 가벼운 금속"},
    {"name": "붕소", "symbol": "B", "description": "비료와 세라믹 유리에 사용"},
    {"name": "탄소", "symbol": "C", "description": "모든 유기물의 기본 구성 원소"},
    {"name": "질소", "symbol": "N", "description": "대기의 약 78%를 차지하는 기체"},
    {"name": "산소", "symbol": "O", "description": "호흡에 필수적인 기체"},
    {"name": "플루오린", "symbol": "F", "description": "가장 반응성이 큰 할로젠 원소"},
    {"name": "네온", "symbol": "Ne", "description": "광고용 간판에 사용되는 불활성 기체"},
    {"name": "나트륨", "symbol": "Na", "description": "소금의 주요 구성 성분"},
    {"name": "마그네슘", "symbol": "Mg", "description": "항공기와 폭죽에 사용되는 금속"},
    {"name": "알루미늄", "symbol": "Al", "description": "가벼운 금속으로 캔, 창틀 등에 사용"},
    {"name": "규소", "symbol": "Si", "description": "반도체 산업에 필수적인 원소"},
    {"name": "인", "symbol": "P", "description": "DNA와 뼈의 구성 성분"},
    {"name": "황", "symbol": "S", "description": "화약, 비료, 성냥 등에 사용"},
    {"name": "염소", "symbol": "Cl", "description": "소독제로 사용되며 자극적인 냄새가 남"},
    {"name": "아르곤", "symbol": "Ar", "description": "불활성 기체로 백열등에 사용"},
    {"name": "칼륨", "symbol": "K", "description": "세포 내 이온 균형 유지에 중요"},
    {"name": "칼슘", "symbol": "Ca", "description": "뼈와 치아의 구성 성분"},
]

# --- 상태 변수 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "questions" not in st.session_state:
    st.session_state.questions = random.sample(elements, 10)
if "answered" not in st.session_state:
    st.session_state.answered = False
if "selected_answer" not in st.session_state:
    st.session_state.selected_answer = ""

# --- 타이틀
st.title("🔬 원소의 특징을 보고 원소 맞추기 퀴즈")
st.write("10문제 랜덤 객관식 퀴즈입니다. 정답을 맞히면 축포가 터집니다!")

# --- 문제 출제
if st.session_state.current_q < 10:
    q = st.session_state.questions[st.session_state.current_q]
    choices = random.sample([el["name"] for el in elements if el["name"] != q["name"]], 3) + [q["name"]]
    random.shuffle(choices)

    st.markdown(f"**Q{st.session_state.current_q+1}.** {q['description']}")
    selected = st.radio("정답을 고르세요", choices, key=f"radio_{st.session_state.current_q}")

    if not st.session_state.answered:
        if st.button("제출하기"):
            st.session_state.selected_answer = selected
            st.session_state.answered = True
            if selected == q["name"]:
                st.success("정답입니다! 🎉")
                st.session_state.score += 1
                st.balloons()
            else:
                st.error(f"오답입니다. 정답은 {q['name']}입니다.")

    else:
        if st.button("다음 문제"):
            st.session_state.current_q += 1
            st.session_state.answered = False
            st.session_state.selected_answer = ""
            st.rerun()

else:
    st.subheader("🎓 퀴즈 종료")
    st.write(f"총 점수: **{st.session_state.score} / 10**")
    if st.button("다시 시작하기"):
        st.session_state.score = 0
        st.session_state.current_q = 0
        st.session_state.questions = random.sample(elements, 10)
        st.session_state.answered = False
        st.rerun()

