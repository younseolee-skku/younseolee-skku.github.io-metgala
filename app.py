import streamlit as st
import streamlit.components.v1 as components

# 화면 꽉 차게 설정
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown("<style>.block-container { padding: 0 !important; } iframe { width: 100vw; height: 100vh; border: none; }</style>", unsafe_allow_html=True)

# 깃허브 기본 주소
base_url = "https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/"

# index.html 읽기
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# [중요] 은서님이 가진 모든 이미지 파일 이름 리스트
image_files = [
    "chanel1.jpeg", "chanel2.jpg", "chanel3.jpg",
    "dior1.jpg", "dior2.jpg", "dior3.jpg", "dior4.jpg", "dior5.jpg", "dior6.jpg",
    "jennie1.webp", "jennie2.webp", "jennie3.webp",
    "jisoo1.webp", "jisoo2.webp", "jisoo3.webp",
    "lisa1.webp", "lisa2.webp", "lisa3.webp",
    "rose1.webp", "rose2.webp", "rose3.webp"
]

# 여기서 자동으로 사진 20장의 주소를 각각 다르게 만들어줍니다!
for img in image_files:
    # 깃허브의 사진 전체 주소
    full_url = f"{base_url}{img}"
    
    # HTML 속의 "chanel1.jpeg" 같은 이름을 찾아서 "https://raw.../chanel1.jpeg"로 싹 바꿉니다.
    html_content = html_content.replace(f'src="{img}"', f'src="{full_url}"')
    html_content = html_content.replace(f"src='{img}'", f'src="{full_url}"')

# 완성된 HTML을 화면에 띄우기
components.html(html_content, height=4000, scrolling=True)
