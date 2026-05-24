import streamlit as st
import streamlit.components.v1 as components
import os

# 1. 이미지가 있는 폴더 확인 (현재 프로젝트 루트 폴더)
# 2. 이미지 파일들을 읽어서 Streamlit이 인식하게 함
# (이미지가 파일명으로 바로 쓰일 수 있도록 환경을 잡아주는 과정입니다)

st.set_page_config(layout="wide")

# index.html 파일 읽기
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# 3. HTML 렌더링
components.html(html_data, height=2000, scrolling=True)
