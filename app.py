import streamlit as st
import streamlit.components.v1 as components

# 페이지 레이아웃 설정
st.set_page_config(layout="wide")

# index.html을 그대로 읽어서 화면에 띄웁니다
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# 화면에 렌더링
components.html(html_data, height=2000, scrolling=True)
