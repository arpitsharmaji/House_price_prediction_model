from pydantic import BaseModel
from typing import Optional

class InputData(BaseModel):
    area_sqft: Optional[int]=None
    bedrooms: Optional[int]=None
    bathrooms: Optional[int]=None
    age: Optional[int]=None
    location: Optional[str]=None
    
    
    
class taskresponseschema(BaseModel):
    id : Optional[int]=None
    area_sqft: Optional[int]=None
    bedrooms: Optional[int]=None
    bathrooms: Optional[int]=None
    age: Optional[int]=None
    location: Optional[str]=None
    user_id: Optional[int]=None
    
    
    