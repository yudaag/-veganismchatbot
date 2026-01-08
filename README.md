# 🌱 비거니즘 챗봇 (Eco Veganism Chatbot)

식품 라벨을 분석하여 비건 식단 호환성, 알레르기 정보, 칼로리, 환경 영향을 제공하는 AI 챗봇입니다.

## 📋 목차

- [소개](#소개)
- [주요 기능](#주요-기능)
- [기술 스택](#기술-스택)
- [설치 방법](#설치-방법)
- [환경 설정](#환경-설정)
- [사용 방법](#사용-방법)
- [프로젝트 구조](#프로젝트-구조)
- [주요 기능 상세](#주요-기능-상세)

## 소개

**이오(Eco)**는 식품 라벨을 바탕으로 성분을 분석하고, 식이 기준에 부합하는지 확인해주는 AI 챗봇입니다. 사용자의 비건 유형과 알레르기 정보를 고려하여 맞춤형 분석을 제공하며, LCA(생애주기평가) 기반 환경 영향까지 함께 분석합니다.

### 챗봇 이름의 의미

"이오"는 '이롭다'와 '오래가다'를 결합한 순한글 이름으로, 사람과 지구 모두에게 이로운 선택이 오래 지속되길 바라는 마음을 담았습니다.

## 주요 기능

### 1. 🏠 시작 페이지
- 챗봇 소개 및 사용 안내
- 깔끔한 UI/UX 디자인

### 2. 📝 사용자 정보 입력
- 단계별 정보 수집 (이름, 성별, 나이, 비건 종류, 알레르기)
- 진행률 표시
- 다양한 비건 유형 지원:
  - 프루테리언
  - 비건
  - 락토
  - 오보
  - 락토오보

### 3. 🤖 챗봇 기능
- **식품 라벨 OCR**: Google Cloud Vision API를 사용한 텍스트 추출
- **성분 분석**: 식품표시기준 기반 성분 분석
- **비건 호환성 확인**: 사용자의 비건 유형에 따른 식품 호환성 분석
- **알레르기 검사**: 알레르기 유발 성분 확인
- **칼로리 정보**: 제품의 칼로리 및 영양 정보 제공
- **환경 영향 분석**: LCA 기반 환경 영향 데이터 제공
  - 생물학적 영향
  - 대기 영향
  - 토지 영향
  - 수자원 영향
- **환경 점수 계산**: 환경 영향 항목별 점수 계산

## 기술 스택

### 프론트엔드
- **Streamlit**: 웹 애플리케이션 프레임워크

### 백엔드 & AI
- **LangChain**: RAG(Retrieval Augmented Generation) 구현
- **FAISS**: 벡터 데이터베이스 (의미 검색)
- **OpenAI API**: 
  - `text-embedding-3-large`: 텍스트 임베딩
  - `ChatOpenAI`: 대화형 AI 모델
- **Google Cloud Vision API**: 이미지 OCR 처리

### 데이터 처리
- **Pandas**: 데이터프레임 처리
- **NumPy**: 수치 연산

## 설치 방법

### 1. 저장소 클론
```bash
git clone <repository-url>
cd -veganismchatbot-main
```

### 2. 가상환경 생성 및 활성화 (권장)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

## 환경 설정

### 1. 환경 변수 파일 생성
프로젝트 루트에 `.env` 파일을 생성하고 다음 정보를 입력하세요:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 2. Streamlit Secrets 설정
Streamlit Cloud를 사용하는 경우, 또는 로컬에서 `.streamlit/secrets.toml` 파일을 생성하여 다음 정보를 설정하세요:

```toml
OPENAI_API_KEY = "your_openai_api_key_here"

[google_credentials]
type = "service_account"
project_id = "your_project_id"
private_key_id = "your_private_key_id"
private_key = "your_private_key"
client_email = "your_client_email"
client_id = "your_client_id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "your_client_x509_cert_url"
```

### 3. FAISS 데이터베이스
`faiss_db_merged.zip` 파일이 프로젝트 루트에 있어야 합니다. 압축 해제는 자동으로 처리됩니다.

## 사용 방법

### 애플리케이션 실행
```bash
streamlit run main.py
```

브라우저에서 `http://localhost:8501`로 접속하여 사용할 수 있습니다.

### 사용 흐름
1. **시작 페이지**: "GET STARTED" 버튼 클릭
2. **정보 입력**: 단계별로 사용자 정보 입력
3. **챗봇 사용**:
   - 식품 라벨 이미지 업로드 (PNG, JPG, JPEG)
   - OCR 자동 처리
   - 질문 입력 예시:
     - "이 제품의 성분을 분석해줘"
     - "비건인가요?"
     - "알레르기 유발 성분이 있나요?"
     - "칼로리는 얼마인가요?"
     - "환경 영향은 어떤가요?"
     - "수자원 영향은?"

## 프로젝트 구조

```
-veganismchatbot-main/
├── main.py              # 메인 애플리케이션 진입점
├── start.py             # 시작 페이지
├── infoslide.py         # 사용자 정보 입력 페이지
├── chatbot.py           # 챗봇 메인 로직
├── info.py              # 사용자 정보 수정 페이지
├── requirements.txt     # Python 패키지 의존성
├── faiss_db_merged.zip  # FAISS 벡터 데이터베이스
├── 제목.png             # 챗봇 아이콘 이미지
└── README.md            # 프로젝트 문서
```

## 주요 기능 상세

### 1. OCR 처리
- Google Cloud Vision API를 사용하여 식품 라벨에서 텍스트 추출
- 업로드된 이미지를 자동으로 분석

### 2. RAG 기반 답변 생성
- FAISS 벡터 데이터베이스에서 관련 문서 검색
- 검색된 문서와 OCR 텍스트를 기반으로 답변 생성
- 사용자의 비건 유형과 알레르기 정보를 고려한 맞춤형 답변

### 3. 질문 유형별 처리
- **성분 분석**: 식품표시기준.pdf 기반
- **비건 호환성**: 식이범위.pdf 기반
- **알레르기**: 알러지.pdf 기반
- **환경 영향**: AGRIBALYSE.csv 기반
- **수자원**: 수자원문서.pdf 기반
- **칼로리**: 칼로리.pdf 기반

### 4. 환경 영향 분석
- 식품 하위 그룹별 필터링
- OCR 텍스트와 제품명 유사도 비교
- 환경 영향 카테고리별 데이터 추출 및 표시
- 환경 영향 점수 계산 (mPt 단위)

### 5. 칼로리 추적
- 질문에서 g 단위 추출
- 칼로리 정보 자동 저장
- 일일 총 칼로리 합계 조회 기능

## 주의사항

- OpenAI API 키와 Google Cloud Vision API 인증 정보가 필요합니다.
- FAISS 데이터베이스 파일(`faiss_db_merged.zip`)이 필요합니다.
- 인터넷 연결이 필요합니다 (API 호출용).

## 라이선스

이 프로젝트는 교육 및 연구 목적으로 제작되었습니다.

## 기여

버그 리포트나 기능 제안은 이슈로 등록해주세요.

---

© 2025 Eco Veganism Chatbot | 이오(io)
