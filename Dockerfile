# Streamlit + ChromaDB를 위한 Python 3.10 환경
FROM python:3.10-slim

# 필수 OS 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 복사 후 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 코드 복사
COPY . .

# Streamlit 실행
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
