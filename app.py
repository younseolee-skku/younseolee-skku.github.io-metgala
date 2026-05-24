import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# CSS로 빈틈 없애기
st.markdown("""
    <style>
        .block-container { padding: 0 !important; }
        iframe { width: 100vw; height: 100vh; border: none; }
    </style>
""", unsafe_allow_html=True)

# 깃허브 경로
base_url = "https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/"

# index.html 읽기
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 이미지 파일 리스트
image_files = [
    "chanel1.jpeg", "chanel2.jpg", "chanel3.jpg",
    "dior1.jpg", "dior2.jpg", "dior3.jpg", "dior4.jpg", "dior5.jpg", "dior6.jpg",
    "jennie1.webp", "jennie2.webp", "jennie3.webp",
    "jisoo1.webp", "jisoo2.webp", "jisoo3.webp",
    "lisa1.webp", "lisa2.webp", "lisa3.webp",
    "rose1.png", "rose1.webp", "rose2.webp", "rose3.webp"
]

# 여기서 핵심! 파일명만 있는걸 주소 형태로 강제 교체합니다.
for img in image_files:
    # src="chanel1.jpeg" 형태를 src="https://raw.../chanel1.jpeg"로 교체
    old_src = f'src="{img}"'
    new_src = f'src="{base_url}{img}"'
    html_content = html_content.replace(old_src, new_src)

components.html(html_content, height=4000, scrolling=True)
