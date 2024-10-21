from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models.base import Base

DATABASE_URL = "postgresql+asyncpg://test:123321@localhost/test"

engine = create_async_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, class_=AsyncSession, expire_on_commit=False, autoflush=False, bind=engine)

def get_db():
    async with SessionLocal() as db:
        yield db