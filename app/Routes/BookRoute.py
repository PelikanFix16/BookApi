from fastapi import APIRouter, Depends, HTTPException,Query
from typing import List,Optional
from fastapi.responses import RedirectResponse,JSONResponse
from app.Core.Schemas.Book import BookBase,BookTitleQuery
from sqlalchemy.orm import Session
from app.database.db_connect import get_db
from app.Core.Models.Book import Book
from app.database.CRUD.Books import create_book,get_book_by_book_id,update_book,get_all_books
from app.Routes import BookRoute
from app.Services.LoadData import GetBooks
from app.Services.CompareBooks import CompareBooks
from app.Services.GenerateBookSchema import GenerateBookSchema

router = APIRouter(
    prefix="/books",
    tags=["Books"],
    responses={404: {"description": "Not found"}},
)


@router.get("/",response_model=List[BookBase])
def getAll(db:Session = Depends(get_db),published_date:Optional[List[int]] = Query(None)):
    print(published_date)
    books = get_all_books(db)
    return books





@router.post("/")
def root(query:BookTitleQuery,db:Session = Depends(get_db)):
    books = GetBooks(query.q)
    BookSchemasList = GenerateBookSchema(books["items"])
    for book_compare in BookSchemasList:
        book = get_book_by_book_id(db,book_compare.book_id)
        if book == None:
            create_book(db,book_compare)
            continue
        if CompareBooks(book_compare,book):
            update_book(db,book_compare)
    url = router.url_path_for("getAll")
    return JSONResponse(content={"books":url})

            

            
    






    

