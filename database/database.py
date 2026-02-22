import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

# TODO: 현재 세션을 직접 생성중. get_db를 사용하여 의존성 주입 구조로 수정

load_dotenv()

# 환경 변수 읽기 - 초기 설정용 추후 config 기반으로 일괄 관리로 변경 예정. 
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

# URL 구성. 
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# 클라이언트는 기본인 psycopg2를 사용하여 사용할 db만 명시

#엔진 및 세션 설정
engine= create_engine(SQLALCHEMY_DATABASE_URL) # 데이터 베이스와 연결 통로
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # 테이터베이스에 데이터를 넣고 뺄때 쓰는 도구
'''
autocommit=False : 별도 커밋 명령이 없으면 커밋 실행 X
autoflush=False : 데이터를 DB에 자동으로 보내지 않음.
'''

# 베이스 클래스 생성. 
Base = declarative_base() # 파이썬 클래스를 DB 테이블로 변환하는 기준

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db  # 실제 로직에서 db 세션을 사용하도록 전달
    finally:
        db.close()  # 요청이 끝나면 무조건 세션을 닫음