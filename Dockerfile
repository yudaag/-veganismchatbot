FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지 설치 및 SQLite 3.47 빌드
RUN apt-get update && apt-get install -y \
    build-essential \
    libreadline-dev \
    curl \
    && curl -O https://www.sqlite.org/2024/sqlite-autoconf-3470000.tar.gz \
    && tar xzf sqlite-autoconf-3470000.tar.gz \
    && cd sqlite-autoconf-3470000 \
    && ./configure --prefix=/usr/local \
    && make && make install \
    && cd .. && rm -rf sqlite-autoconf-3470000 sqlite-autoconf-3470000.tar.gz \
    && apt-get remove -y build-essential libreadline-dev \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# 환경 변수 설정
ENV LD_LIBRARY_PATH=/usr/local/lib

# Python 패키지 설치
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 포트 개방 및 Streamlit 실행
EXPOSE 8501
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
