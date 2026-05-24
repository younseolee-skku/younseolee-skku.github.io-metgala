import streamlit as st
import streamlit.components.v1 as components

# 화면 설정
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown("<style>.block-container { padding: 0 !important; } iframe { width: 100vw; height: 100vh; border: none; }</style>", unsafe_allow_html=True)

# 1. HTML 파일 읽기
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# 2. 여기에 은서님이 링크를 직접 붙여넣으세요! (한 줄에 하나씩)
# 폼: html_data = html_data.replace('기존파일명', '직접복사한주소')
html_data = html_data.replace('chanel1.jpeg', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/chanel1.jpeg')
html_data = html_data.replace('chanel2.jpg', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/chanel2.jpg')
html_data = html_data.replace('chanel3.jpg', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/chanel3.jpg')
html_data = html_data.replace('dior1.jpg', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/dior1.jpg')
html_data = html_data.replace('dior2.jpg', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/dior2.jpg')
html_data = html_data.replace('dior3.jpg', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/dior3.jpg')
html_data = html_data.replace('dior4.jpg', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/dior4.jpg')
html_data = html_data.replace('dior5.jpg', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/dior5.jpg')
html_data = html_data.replace('dior6.jpg', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/dior6.jpg')
html_data = html_data.replace('jennie1.webp', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/jennie1.webp')
html_data = html_data.replace('jennie2.webp', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/jennie2.webp')
html_data = html_data.replace('jennie3.webp', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/jennie3.webp')
html_data = html_data.replace('jisoo1.webp', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/jisoo1.webp')
html_data = html_data.replace('jisoo2.webp', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/jisoo2.webp')
html_data = html_data.replace('jisoo3.webp', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/jisoo3.webp')
html_data = html_data.replace('lisa1.webp', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/lisa1.webp')
html_data = html_data.replace('lisa2.webp', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/lisa2.webp')
html_data = html_data.replace('lisa3.webp', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/lisa3.webp')
html_data = html_data.replace('rose1.png', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/rose1.png')
html_data = html_data.replace('rose2.webp', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/rose2.webp')
html_data = html_data.replace('rosee3.webp', 'https://raw.githubusercontent.com/younseolee-skku/younseolee-skku.github.io-metgala/main/rose3.webp')





# 3. 화면 띄우기
components.html(html_data, height=4000, scrolling=True)
