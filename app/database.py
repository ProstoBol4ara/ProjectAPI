from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, delete

DATABASE_URL = "postgresql+asyncpg://test:123321@localhost:5432/test"

engine = create_async_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, class_=AsyncSession, expire_on_commit=False, autoflush=False, bind=engine)

async def get_db():
    async with SessionLocal() as db:
        yield db