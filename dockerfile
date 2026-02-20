# 1. 베이스 이미지 설정 
FROM python:3.10-slim

# 2. 컨테이너 내부의 작업 디렉토리 설정
WORKDIR /app
# 3. 컴파일러 등 설치 - DB 연결 등을 위한 빌드 도구 - 추후 빌드 단계와 서비스 단계를 분리하여 이미지 용량 관리 필요
RUN apt-get update && apt-get install -y gcc && apt-get install -y curl

# 4. 의존성 관리용 poetry 설치
RUN pip install poetry 

# 5.poetry의 의존성 관리 파일 pyproject.toml, poetry.lock 복사 
# 도커파일과 같은 위치의 두 파일을 WORKDIR로 복사
COPY pyproject.toml poetry.lock ./

#6. 가상환경 생성하지 않고 시스템 환경에 바로 설치 - 도커파일용
# --no-interaction : 사용자에 대한 질문 삭제, --no-ansi : 로그를 단순 텍스트로만 출력
RUN poetry config virtualenvs.create false \ 
    && poetry install --no-interaction --no-ansi 

# 7. 나머지 소스 코드 전체 복사 (호스트 -> WORKDIR) 
COPY . .

# 예시 주석: 호스트의 backend 폴더를 컨테이너 내의 /app/imagebackend 폴더로 복사하고 싶을 때
# COPY ./backend ./imagebackend

# 8. FastAPI 애플리케이션 실행 명령어
# 127.0.0.1 : local host, 0.0.0.0 : 모든 네트워크 접속 허용 
# 따라서 컨테이너에 앱을 실행할 경우 127.0.0.1을 통해 app를 실행할 경우 접속이 안됨
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]