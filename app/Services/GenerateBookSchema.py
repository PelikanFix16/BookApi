from pydantic import validate_arguments, ValidationError
from app.Core.Schemas.Book import BookBase
@validate_arguments
def GenerateBookSchema(books):
    book_arr = []
    for book in books:
        title = book["volumeInfo"]["title"]
        try:
            author = book["volumeInfo"]["authors"]
        except:
            author = []
        publish_date = int(book["volumeInfo"]["publishedDate"][0:4])
        try:
            categories = book["volumeInfo"]["categories"]
        except:
            categories = []
        try:
            avarage_rating = float(book["volumeInfo"]["averageRating"])
        except:
            avarage_rating = 0.0

        try:
            ratings_count = int(book["volumeInfo"]["ratingsCount"])
        except:
            ratings_count = 0
        
        try:
            thubnail = book["volumeInfo"]["imageLinks"]["thumbnail"]
        except:
            thubnail = ""
        book_id = book["id"]

        book_arr.append(
            BookBase(title=title,authors=author,
            published_date=publish_date,categories=categories,
            average_rating=avarage_rating,ratings_count=ratings_count,
            thumbnail=thubnail,book_id=book_id)
        )
    return book_arr



