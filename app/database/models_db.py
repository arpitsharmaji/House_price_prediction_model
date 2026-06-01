from sqlalchemy import Column, Integer, Float, String,ForeignKey
from app.database.db import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    area_sqft = Column(Float)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    age = Column(Integer)
    location = Column(String)
    prediction = Column(Float)
    
    user_id = Column(Integer,ForeignKey("user_table.id", ondelete="CASCADE"))
    