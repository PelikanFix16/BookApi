from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database.db_connect import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer,primary_key=True)
    title = Column(String,nullable=False)
    description = Column(String,nullable=False)
    