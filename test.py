import os
import zipfile
import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma

st.title("Chroma 벡터스토어 로드 테스트")

persist_dir = "./veganchroma_db"
zip_path = "veganchroma_db.zip"

# 압축 해제
if not os.path.exists(persist_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(persist_dir)
    st.write("✅ Chroma DB 압축 해제 완료")

try:
    embedding_function = OpenAIEmbeddings(model="text-embedding-3-large")
    vectorstore = Chroma(
        persist_directory=persist_dir,
        embedding_function=embedding_function
    )
    st.success("✅ 벡터스토어 로드 성공!")
except Exception as e:
    st.error(f"❌ 벡터스토어 로드 실패: {e}")
