from sqlalchemy.orm import Session
from app.Core.Models.Book import Book
from app.Core.Schemas.Book import BookBase

def create_book(db:Session,book:BookBase):
    db_book = Book(title=book.title,authors=book.authors,published_date=book.published_date,categories=book.categories,average_rating=book.average_rating,ratings_count=book.ratings_count,thumbnail=book.thumbnail,book_id=book.book_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book



