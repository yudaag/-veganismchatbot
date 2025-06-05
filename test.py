import streamlit as st
import os, zipfile, traceback, tempfile
from langchain_chroma import Chroma  # langchain_chroma로 임포트 변경 가능성 확인
from langchain.embeddings import OpenAIEmbeddings

st.title("🧠 Chroma 벡터스토어 로드 확인")

zip_path = "veganchroma_db.zip"
extract_path = os.path.join(tempfile.gettempdir(), "veganchroma_db")

if not os.path.exists(os.path.join(extract_path, "chroma.sqlite3")):
    if os.path.exists(zip_path):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            st.success("✅ Chroma DB 압축 해제 완료")
        except Exception as e:
            st.error(f"❌ 압축 해제 실패: {e}")
            st.text(traceback.format_exc())
    else:
        st.error(f"❌ 압축파일 {zip_path}를 찾을 수 없습니다.")
else:
    st.info("📁 이미 압축 해제됨")

try:
    embedding_function = OpenAIEmbeddings(model="text-embedding-3-large")
    vectorstore = Chroma(persist_directory=extract_path, embedding_function=embedding_function)
    st.success("✅ 벡터스토어 로드 성공")
except Exception as e:
    st.error(f"❌ 벡터스토어 로드 실패: {e}")
    st.text(traceback.format_exc())
