from typing import Any
import chromadb
from chromadb.config import Settings
import pandas as pd

class ChromaDBConnection:
    def __init__(self, client_type="PersistentClient", path=None, host=None, port=None, ssl=False):
        self.client_type = client_type
        self.path = path
        self.host = host
        self.port = port
        self.ssl = ssl
        self.client = None

    def _connect(self):
        if self.client_type == "PersistentClient":
            self.client = chromadb.Client(Settings(
                chroma_db_impl="duckdb+parquet",
                persist_directory=self.path
            ))
        elif self.client_type == "HttpClient":
            self.client = chromadb.HttpClient(
                host=self.host,
                port=self.port,
                ssl=self.ssl
            )
        else:
            raise ValueError(f"Unsupported client_type: {self.client_type}")

    def get_collection_data(self, collection_name: str) -> pd.DataFrame:
        collection = self.client.get_collection(collection_name)
        # 컬렉션에서 임베딩 + 문서 등 데이터프레임으로 반환
        return pd.DataFrame(collection.get(include=["metadatas", "documents", "embeddings"]))

    def create_collection(self, collection_name: str, embedding_function_name: str = "DefaultEmbedding"):
        self.client.create_collection(name=collection_name, embedding_function_name=embedding_function_name)

    def delete_collection(self, collection_name: str):
        self.client.delete_collection(name=collection_name)

    def upload_document(self, directory: str, collection_name: str, file_paths: list[str]):
        collection = self.client.get_collection(collection_name)
        # 여기에 Langchain DocumentLoader 등으로 파일 읽어 임베딩 생성 후 업로드 구현 필요
        # 예시 생략 (상황에 맞게 작성)

    def retrieve(self, collection_name: str, query: str):
        collection = self.client.get_collection(collection_name)
        results = collection.query(query_texts=[query], n_results=10)
        # 결과를 DataFrame 등으로 변환해서 반환 (상황에 맞게 작성)
        return pd.DataFrame(results["documents"])
