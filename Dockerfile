# 베이스 이미지
FROM python:3.10-slim

# 작업 디렉토리 생성
WORKDIR /app

# 시스템 패키지 설치 (build-essential, libsqlite3 등)
RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# requirements 복사 및 설치
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 앱 코드 복사
COPY . .

# 포트 개방 및 streamlit 실행
EXPOSE 8501
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

