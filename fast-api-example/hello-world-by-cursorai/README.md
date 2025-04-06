# FastAPI Hello World 예제

이 프로젝트는 CursorAI의 에이전트를 이용해 자동으로 생성된 FastAPI 기반의 Hello World 예제입니다.

## 최초 요구사항

```
파이썬 3.12 기준을 사용하고, 환경은 uv 로 venv 잡아서 작업해주고, fastapi로 hello world 를 리턴하는 코드와 테스트코드도 함께 작성해서 이걸 도커로 만들어줘. 그리고 잘 실행되는지도 확인해줘.
```

## 프로젝트 구조

```
.
├── README.md
├── Dockerfile
├── main.py
├── requirements.txt
└── test_main.py
```

## 기술 스택

- Python 3.12
- FastAPI 0.109.2
- uvicorn 0.27.1
- pytest 8.0.0
- Docker

## 개발 환경 설정

1. uv를 사용하여 가상환경 생성 및 패키지 설치:

```bash
# 가상환경 생성
uv venv

# 가상환경 활성화 및 패키지 설치
source .venv/bin/activate
uv pip install -r requirements.txt
```

## 실행 방법

### 로컬 실행

```bash
# 서버 실행
uvicorn main:app --reload
```

### Docker 실행

```bash
# Docker 이미지 빌드
docker build -t fastapi-hello-world .

# Docker 컨테이너 실행
docker run -p 8000:8000 fastapi-hello-world
```

## API 엔드포인트

- `GET /`: Hello World 메시지를 반환
  - 응답: `{"message": "Hello World"}`
- `GET /docs`: Swagger UI 문서 (FastAPI 자동 생성)

## 테스트

```bash
# 테스트 실행
pytest test_main.py -v
```

## 자동 생성된 파일 설명

이 프로젝트의 모든 파일들은 CursorAI의 에이전트를 통해 자동으로 생성되었습니다:

- `main.py`: FastAPI 애플리케이션의 메인 코드
- `test_main.py`: API 엔드포인트 테스트 코드
- `requirements.txt`: 프로젝트 의존성 정의
- `Dockerfile`: Docker 컨테이너 설정
- `README.md`: 프로젝트 문서화

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다. 