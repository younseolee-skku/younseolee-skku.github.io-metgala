import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# 1. 깃허브 리포지토리의 Raw 이미지 기본 경로
# (은서님의 리포지토리 주소에 맞춰 설정했습니다)
base_url = "https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/"

# 2. 가진 이미지 파일 목록
image_files = [
    "chanel1.jpeg", "chanel2.jpg", "chanel3.jpg",
    "dior1.jpg", "dior2.jpg", "dior3.jpg", "dior4.jpg", "dior5.jpg", "dior6.jpg",
    "jennie1.webp", "jennie2.webp", "jennie3.webp",
    "jisoo1.webp", "jisoo2.webp", "jisoo3.webp",
    "lisa1.webp", "lisa2.webp", "lisa3.webp",
    "rose1.png", "rose1.webp", "rose2.webp", "rose3.webp"
]

# 3. index.html 파일 읽기
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# 4. 이미지 경로 자동 치환
for img in image_files:
    # index.html 안의 src="파일명"을 찾아 src="깃허브주소/파일명"으로 바꿉니다.
    html_data = html_data.replace(f'src="{img}"', f'src="{base_url}{img}"')

# 5. 화면에 띄우기
components.html(html_data, height=3000, scrolling=True)
