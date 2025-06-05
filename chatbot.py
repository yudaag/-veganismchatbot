import streamlit as st
import os
import zipfile

# 절대 경로로 경로 설정
project_root = os.path.dirname(os.path.abspath(__file__))  # 현재 스크립트 기준
zip_path = os.path.join(project_root, "faiss_db_merged.zip")
persist_dir = os.path.join(project_root, "faiss_db_merged")

# 압축 해제
if not os.path.exists(persist_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(persist_dir)
        st.success("✅ FAISS DB 압축 해제 완료")

# 내부 파일 확인 (streamlit에 표시)
try:
    files = os.listdir(persist_dir)
    st.text(f"📄 압축 해제 후 포함된 파일: {files}")
    if "index.faiss" not in files:
        st.warning("❌ index.faiss 없음! 경로 문제 확인 필요")
except Exception as e:
    st.error(f"📛 디렉토리 확인 중 오류: {e}")

# FAISS 로드
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

embedding_function = OpenAIEmbeddings(model="text-embedding-3-large")
st.session_state["vectorstore"] = FAISS.load_local(
    persist_dir,
    embedding_function,
    allow_dangerous_deserialization=True
)
