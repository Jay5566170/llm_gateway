from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database.base import Base


class RequestLog(Base):

    __tablename__ = "request_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    prompt = Column(
        Text,
        nullable=False
    )

    response = Column(
        Text,
        nullable=False
    )

    provider = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )