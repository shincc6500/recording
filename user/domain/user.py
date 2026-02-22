from dataclasses import dataclass
from datetime import datetime

@dataclass
class Profile:
    name : str # 유저 이름 
    email : str # 유저 이메일
    memo: str | None # 유저 자기소개 (선택사항)

@dataclass 
class User: 
    id : str # ulid 
    username: str # 로그인용
    password : str    
    role : int # 등급 단위 관리값  
    profile : Profile # 개인정보  
    created_at: datetime
    updated_at : datetime

