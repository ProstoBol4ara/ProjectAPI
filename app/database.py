from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from fastapi import Depends

DATABASE_URL = "postgresql://test:123321@localhost/test"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_depends():
    return Depends(get_db)