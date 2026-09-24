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


# Load models
from app.models.request_log import RequestLog


print("Tables detected:", Base.metadata.tables.keys())


Base.metadata.create_all(bind=engine)


print("Table creation finished")