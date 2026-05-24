import streamlit as st
import streamlit.components.v1 as components

# 1. 화면을 꽉 차게 만들고, 스트림릿 메뉴/헤더를 숨기는 설정
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# 마법의 CSS: 스트림릿의 여백과 메뉴를 싹 지웁니다.
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        iframe {
            width: 100vw;
            height: 100vh;
            border: none;
        }
    </style>
    """, unsafe_allow_html=True)

# 2. 깃허브 이미지 기본 경로
base_url = "https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/"

# 3. 은서님의 파일 목록 (보내주신 사진 보고 다 적었습니다!)
image_files = [
    "chanel1.jpeg", "chanel2.jpg", "chanel3.jpg",
    "dior1.jpg", "dior2.jpg", "dior3.jpg", "dior4.jpg", "dior5.jpg", "dior6.jpg",
    "jennie1.webp", "jennie2.webp", "jennie3.webp",
    "jisoo1.webp", "jisoo2.webp", "jisoo3.webp",
    "lisa1.webp", "lisa2.webp", "lisa3.webp",
    "rose1.png", "rose1.webp", "rose2.webp", "rose3.webp"
]

# 4. index.html 읽기
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# 5. 이미지 경로 자동 변환 (건드릴 필요 없음!)
for img in image_files:
    html_data = html_data.replace(f'src="{img}"', f'src="{base_url}{img}"')

# 6. 화면 전체에 꽉 채워서 띄우기
components.html(html_data, height=4000, scrolling=True)
