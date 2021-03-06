from sqlalchemy.orm import Session
from app.Core.Models.Book import Book
from app.Core.Schemas.Book import BookBase
from typing import List
import json
from sqlalchemy import func


def create_book(db:Session,book:BookBase):
    db_book = Book(title=book.title,authors=book.authors,published_date=book.published_date,categories=book.categories,average_rating=book.average_rating,ratings_count=book.ratings_count,thumbnail=book.thumbnail,book_id=book.book_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book



def get_book_by_book_id(db:Session,book_id:str):
    return db.query(Book).filter(Book.book_id == book_id).first()

def update_book(db:Session,book:BookBase):
    book_query = db.query(Book).filter(Book.book_id == book.book_id).first()
    book_query.title = book.title
    book_query.authors = book.authors
    book_query.published_date = book.published_date
    book_query.categories = book.categories
    book_query.average_rating = book.average_rating
    book_query.ratings_count = book.ratings_count
    book_query.thumbnail = book.thumbnail
    db.commit()
    return book_query



def get_all_books(db:Session):
    return db.query(Book).all()

def get_book_by_date(db:Session,date:List[int]):
    if len(date) == 1:
        return db.query(Book).filter(Book.published_date == date[0]).all()
    else:
        return db.query(Book).filter(Book.published_date >= date[0],Book.published_date <= date[1]).all()




def get_books_by_authors(db:Session,authors:str):
    return db.query(Book).filter(func.json_contains(Book.authors,json.dumps([authors])) == 1).all()



