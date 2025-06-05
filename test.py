import streamlit as st
import os
import zipfile
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

st.title("🧠 Chroma 벡터스토어 로드 확인")

# 1. Chroma DB 압축 해제
zip_path = "veganchroma_db.zip"
extract_path = "veganchroma_db"

if not os.path.exists(os.path.join(extract_path, "chroma.sqlite3")):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    st.success("✅ Chroma DB 압축 해제 완료")
else:
    st.info("📁 Chroma DB 이미 압축 해제됨")

# 2. 벡터스토어 로드
try:
    embedding_function = OpenAIEmbeddings(model="text-embedding-3-large")
    vectorstore = Chroma(
        persist_directory=extract_path,
        embedding_function=embedding_function
    )
    st.success("✅ 벡터스토어 로드 성공")
except Exception as e:
    st.error(f"❌ 벡터스토어 로드 실패: {e}")
