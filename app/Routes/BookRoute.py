from fastapi import APIRouter, Depends, HTTPException
from app.Core.Schemas.Book import BookBase
from sqlalchemy.orm import Session
from app.database.db_connect import get_db
from app.Core.Models.Book import Book
from app.database.CRUD.Books import create_book
from app.Routes import BookRoute
from app.Services.LoadData import GetBooks

router = APIRouter(
    prefix="/books",
    tags=["Books"],
    responses={404: {"description": "Not found"}},
)


@router.get("/",response_model=BookBase)
def root(db:Session = Depends(get_db)):
    t = GetBooks("war")
    print(t["items"][0])

