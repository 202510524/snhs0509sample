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

# LaTeX 수식 출력
st.latex(r"E = mc^2")
st.latex(r"\int_{a}^{b} x^2 dx = \frac{b^3 - a^3}{3}")

# 정보성 메시지 박스
st.info("ℹ️ 정보 메시지입니다.")
st.warning("⚠️ 경고 메시지입니다.")
st.success("✅ 성공 메시지입니다.")
st.error("❌ 오류 메시지입니다.")

# 이미지 출력
st.image("https://static.streamlit.io/examples/cat.jpg", caption="귀여운 고양이", use_container_width=True)
st.image("https://via.placeholder.com/300", caption="예시 이미지")

# 영상 출력
st.video("https://www.youtube.com/watch?v=4nU-Fp96p8E")
st.video("https://www.youtube.com/watch?v=B1J6Ou4q8vE")

# 오디오 출력
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 지도 출력
import pandas as pd
df = pd.DataFrame({"lat": [37.5], "lon": [127.0]})
st.map(df, zoom=12)

# 데이터프레임 테이블 출력
st.dataframe(pd.DataFrame({
    "이름": ["홍길동", "김철수"],
    "점수": [85, 92]
}))

st.code("""
import streamlit as st
st.title('Hello World')
""", language="python")

st.link_button("연결할 url을 이 다음 변수에 써주세요!", 'https://docs.streamlit.io/develop/quick-reference/cheat-sheet')

st.image("https://forest-s3.s3.amazonaws.com/uploads/summernote_asset/image/480/%EB%B3%B5%EC%9E%90%EA%B8%B0%EB%82%98%EB%AC%B4-%EC%9D%B8%EC%A0%9C%EC%88%98%EC%82%B0%EB%A6%ACB280910-031.JPG")
st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmE3eHloZjhuazB4OHg1ZmZ1Z3A5c2s5dm1jcDJqc2dsODl5c2ttNiZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/uQgXjl505BdYAv8H0X/giphy.webp")

# st.columns(n): 화면을 n개의 수직 열로 나눕니다
col1, col2 = st.columns(2)  # 2개의 열 생성

with col1:
    st.write("왼쪽 열입니다.")  # 첫 번째 열에 내용 작성
with col2:
    st.write("오른쪽 열입니다.")  # 두 번째 열에 내용 작성

    # st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

with tab1:
    st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
with tab2:
    st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용

    # st.expander("제목"): 내용을 접었다 펼 수 있는 컨테이너입니다
with st.expander("ℹ️ 자세한 설명 보기"):
    st.write("여기에 상세 설명이나 보조 정보를 넣을 수 있습니다.")

    # st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
st.sidebar.title("📌 사이드바 메뉴")
option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
st.write("선택한 옵션:", option)

# st.empty(): 동적으로 내용을 업데이트할 수 있는 빈 컨테이너입니다
placeholder = st.empty()
placeholder.write("잠시 후 이 자리에 내용이 바뀝니다.")

import time
time.sleep(2)
placeholder.write("⏳ 내용이 업데이트되었습니다!")

# st.container(): 특정 영역 안에 여러 컴포넌트를 묶어 배치합니다
with st.container():
    st.subheader("📦 이 영역은 하나의 컨테이너입니다.")
    st.write("여기에 다양한 요소를 넣을 수 있습니다.")
    st.line_chart({"data": [1, 5, 2, 6]})
st.balloons()
st.snow()
name = st.text_input("이름을 입력해주세요.")
if name=="고구마":
    st.success(name+"님 반갑습니다.")
else:
    st.error("고구마님이 나니네요...")


# 여러 옵션 중 하나 선택
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.info("선택한 성별:"+ gender)

# 카메라로 사진 촬영
image_data = st.camera_input("사진을 찍어보세요")
if image_data:
    st.image(image_data)