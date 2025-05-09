import streamlit as st

st.title("🎈 황우성의 첫 번째 앱!")
st.info(
    "안녕하세요! 반갑습니다. 저는 황우성입니다."
)
st.write(
    "안녕하세요! 반갑습니다. 저는 황우성입니다."
)

# st.write(): 가장 기본적인 텍스트 출력 함수입니다
st.write("이것은 기본 텍스트 출력입니다.")

# st.markdown(): 마크다운 문법 지원 (굵게, 기울임, 목록 등)
st.markdown("**굵은 텍스트**, *기울임 텍스트*")
st.markdown("""- 첫 번째 항목
- 두 번째 항목
- 여러 줄을 쓸 때""")

# 페이지 구조용 제목 출력
st.title("메인 제목입니다")
st.header("중간 제목입니다")
st.subheader("하위 제목입니다")
