from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    email = Column(
        String,
        unique=True
    )

    password = Column(String)

class AuditHistory(Base):

    __tablename__ = "audit_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_email = Column(String)

    website_url = Column(String)

    risk_score = Column(Integer)

    created_at = Column(String)