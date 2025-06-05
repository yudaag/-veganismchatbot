import os
import zipfile
import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# ✅ 벡터스토어가 없으면 FAISS로 초기화
if "vectorstore" not in st.session_state:
    zip_path = "/mount/src/-veganismchatbot/faiss_db_merged.zip"
    persist_dir = "/mount/src/-veganismchatbot/faiss_db_merged"

    # 📁 압축 해제
    if not os.path.exists(persist_dir):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(persist_dir)
            print(f"✅ 압축 해제 완료: {persist_dir}")

    # 📂 내부에 다시 디렉토리가 있는 경우 처리
    inner = os.listdir(persist_dir)
    if len(inner) == 1 and os.path.isdir(os.path.join(persist_dir, inner[0])):
        persist_dir = os.path.join(persist_dir, inner[0])
        print(f"📂 이중 구조 감지 → 내부 경로로 이동: {persist_dir}")

    # 🔍 벡터스토어 로드
    embedding_function = OpenAIEmbeddings(model="text-embedding-3-large")
    st.session_state["vectorstore"] = FAISS.load_local(
        persist_dir,
        embedding_function,
        allow_dangerous_deserialization=True
    )
    print("✅ FAISS 로드 완료")
