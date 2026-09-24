from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.base import Base


DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/llm_gateway"


engine = create_engine(
    DATABASE_URL
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Import models here only for table registration
from app.models.request_log import RequestLog
from app.models.conversation import Conversation
from app.models.message import Message


Base.metadata.create_all(bind=engine)