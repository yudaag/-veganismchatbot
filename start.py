import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="", layout="wide", page_icon="🥦")

def show():
    def get_base64_image(image_path):
        with open(image_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    base64_image = get_base64_image("시작.jpeg")

    # CSS
    st.markdown(f"""
        <style>
            html, body, .main {{
                margin: 0;
                padding: 0;
                height: 100%;
                overflow: hidden;
            }}

            .background {{
                position: relative;
                width: 100%;
                height: 70vh;
                background-image: url("data:image/jpeg;base64,{base64_image}");
                background-size: cover;
                background-position: center;
                display: flex;
                align-items: center;
            }}

            .left-blur {{
                width: 100%;
                height: 100%;
                backdrop-filter: blur(30px);
                background-color: rgba(255, 255, 255, 0.6);
                display: flex;
                flex-direction: column;
                padding: 5rem 3rem;
                justify-content: flex-start;
            }}

            .title {{
                font-size: 70px;
                font-weight: bold;
                color: #1b5e20;
                margin-bottom: 1rem;
            }}

            .subtitle {{
                font-size: 30px;
                color: #1b5e20;
                margin-bottom: 1.5rem;
            }}

            .text {{
                font-size: 20px;
                color: #333;
                margin-bottom: 1rem;
            }}

            .footer {{
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                text-align: center;
                background-color: rgba(255, 255, 255, 0.9);
                padding: 12px 0;
                font-size: 14px;
                color: #4f4f4f;
                border-top: 1px solid #cfcfcf;
                z-index: 999;
            }}
        </style>
    """, unsafe_allow_html=True)

    # 배경 + 텍스트 콘텐츠
    st.markdown(f"""
        <div class="background">
            <div class="left-blur">
                <div class="title">이 모든 걸 <br>
                오 분 안에 알려드려요! <br>
                </div>
                <div class="subtitle"><strong>이 제품, 먹어도 될까?</strong></div>
                <div class="text">
                    이오는 제품의 식품 라벨을 바탕으로<br>
                    성분을 분석하고, 식이 기준에 부합하는지 확인해드려요.<br>
                    또한 알레르기 유발 성분 여부와 칼로리 정보,<br>
                    LCA 기반 환경 영향까지 함께 분석해드립니다.<br>
                    지금, 이오와 함께 가볍고 똑똑한 비건 라이프를 시작해보세요.<br>
                </div>
    """, unsafe_allow_html=True)

    # 🔽 버튼 위치 조정용 컬럼: 텍스트 바로 밑에 위치해야 함
    col1, col2, col3 = st.columns([1, 2, 7])
    with col2:
        st.markdown("""
            <style>
            div.stButton > button {
                font-size: 32px;
                padding: 1.2rem 3rem;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                transition: transform 0.2s;
            }

            div.stButton > button:hover {
                background-color: #45a049;
                transform: scale(1.05);
            }
            </style>
        """, unsafe_allow_html=True)

        if st.button("GET STARTED"):
            st.session_state.page = "infoslide"

    # HTML 닫기
    st.markdown("</div></div>", unsafe_allow_html=True)

    # 푸터
    st.markdown("""
        <div class="footer">
            © 2025 Eco Veganism Chatbot | io
        </div>
    """, unsafe_allow_html=True)

