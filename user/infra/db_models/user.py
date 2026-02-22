from datetime import datetime, timezone
from sqlalchemy import String, DateTime, Text, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from database.database import Base

class Profile(Base):
    __tablename__ = "profiles" 

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"),primary_key=True, unique=True)
    name: Mapped[str]= mapped_column(String(36),nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    memo: Mapped[Optional[str]] = mapped_column(Text, nullable=True)   
    
    # 테이블 간의 관계 정의 
    owner: Mapped["User"] = relationship("User", back_populates="profile")

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    username: Mapped[str] = mapped_column(String(36), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    role: Mapped[int] = mapped_column(Integer, nullable=False)

    created_at: Mapped[datetime ]= mapped_column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime ]= mapped_column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc),
                                                  onupdate=lambda: datetime.now(timezone.utc))

    # 테이블 간의 관계 정의 
    profile: Mapped["Profile"] = relationship("Profile", back_populates="owner", uselist=False)

