from app.database.db import Base
from sqlalchemy import Integer, Column, Boolean, DateTime, String,ForeignKey

class usermodel(Base):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    username = Column(String, nullable = False)
    hash_password = Column(String, nullable = False)
    email = Column(String)

    
    
    
    