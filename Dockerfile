# 1. Python 베이스 이미지 선택
FROM python:3.11-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 시스템 패키지 설치 (sqlite3 업그레이드용)
RUN apt-get update && apt-get install -y \
    build-essential \
    sqlite3 \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. requirements.txt 복사 및 설치
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5. 코드 복사
COPY . .

# 6. Streamlit 실행 명령
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
