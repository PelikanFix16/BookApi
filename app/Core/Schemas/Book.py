from typing import List,Optional
from pydantic import BaseModel

class BookBase(BaseModel):
    title:str
    authors:List[str]
    published_date:int
    categories:List[str]
    average_rating:float
    ratings_count:int
    thumbnail:str
    book_id:str
    class Config:
        orm_mode = True
    
    
class BookTitleQuery(BaseModel):
    q:str
