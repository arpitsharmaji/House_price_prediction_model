from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.database import settings

engine = create_engine(url=settings.setttings.DB_CONNECTION)

LocalSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_session():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close()
    