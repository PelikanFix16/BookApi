from fastapi import APIRouter, Depends, HTTPException,Query
from typing import List,Optional
from fastapi.responses import RedirectResponse,JSONResponse
from app.Core.Schemas.Book import BookBase,BookTitleQuery
from sqlalchemy.orm import Session
from app.database.db_connect import get_db
from app.Core.Models.Book import Book
from app.database.CRUD.Books import create_book,get_book_by_book_id,update_book,get_all_books,get_book_by_date,get_books_by_authors
from app.Routes import BookRoute
from app.Services.LoadData import GetBooks
from app.Services.CompareBooks import CompareBooks,CompareArraysBooks
from app.Services.GenerateBookSchema import GenerateBookSchema



router = APIRouter(
    prefix="/books",
    tags=["Books"],
    responses={404: {"description": "Not found"}},
)


@router.get("/",response_model=List[BookBase])
def getAll(db:Session = Depends(get_db),
            published_date:Optional[List[int]] = Query(None),
            sort:Optional[str] = "ASC",
            authors:Optional[List[str]] = Query(None),idBook:Optional[str] = None):
    books = []
    if published_date:
        books.extend(get_book_by_date(db,published_date))
    if authors:
        arr_temp = []
        for i in authors:
            arr_temp.extend(get_books_by_authors(db,i))
        if books:
            new_arr = CompareArraysBooks(arr_temp,books)
            books = new_arr
        else:
            books = arr_temp
        
    if idBook and books == None:
        books.append(get_book_by_book_id(db,idBook))


    if not books:
        books = get_all_books(db)
    
   

    if sort == "ASC":
        books.sort(key=lambda x: x.published_date)
    else:
        books.sort(key=lambda x: x.published_date,reverse=True)
        

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

            

            
    






    

