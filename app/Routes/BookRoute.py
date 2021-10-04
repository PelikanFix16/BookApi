from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from app.Core.Schemas.Book import BookBase,BookTitleQuery
from sqlalchemy.orm import Session
from app.database.db_connect import get_db
from app.Core.Models.Book import Book
from app.database.CRUD.Books import create_book
from app.Routes import BookRoute
from app.Services.LoadData import GetBooks
from app.Services.GenerateBookSchema import GenerateBookSchema

router = APIRouter(
    prefix="/books",
    tags=["Books"],
    responses={404: {"description": "Not found"}},
)


@router.post("/",response_class=RedirectResponse)
def root(query:BookTitleQuery,db:Session = Depends(get_db)):
    books = GetBooks(query.q)
    BookSchemasList = GenerateBookSchema(books["items"])
    #TODO get each book from database with book_id compare and change in database if something is diffrent
    





    

