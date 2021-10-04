from typing import List,Optional
from pydantic import BaseModel

class BookBase(BaseModel):
    title:str
    authors:List[str]
    published_date:int
    categories:List[str]
    average_rating:int
    ratings_count:int
    thumbnail:str
    class Config:
        orm_mode = True
    
    
