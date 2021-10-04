from sqlalchemy import Boolean, Column, ForeignKey, Integer, Text
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from . import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer,primary_key=True)
    title = Column(Text,nullable=False)
    authors = Column(JSON,default=[],nullable=False)
    published_date = Column(Integer,nullable=False)
    categories = Column(JSON,default=[],nullable=False)
    average_rating = Column(Integer,nullable=False)
    ratings_count = Column(Integer,nullable=False)
    thumbnail = Column(Text,nullable=False)
    
