# Python 3.12 슬림 이미지를 베이스로 사용 (경량화된 이미지)
FROM python:3.12-slim

# 작업 디렉토리를 /app으로 설정
WORKDIR /app

# uv 패키지 매니저 설치 (빠른 Python 패키지 설치를 위함)
RUN pip install uv

# 의존성 파일들을 컨테이너로 복사 (캐싱 최적화를 위해 먼저 복사)
COPY pyproject.toml uv.lock ./

# 프로젝트 의존성 설치 (캐시 사용 안함으로 일관된 빌드 보장)
RUN uv sync --no-cache

# 애플리케이션 소스 코드를 컨테이너로 복사
COPY . .

# 컨테이너가 8800 포트에서 요청을 받도록 설정
EXPOSE 8800

# 애플리케이션 실행 명령어 (Uvicorn ASGI 서버로 FastAPI 앱 구동)
CMD ["python", "-m", "uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8800"]


