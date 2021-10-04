import requests 
from pydantic import validate_arguments, ValidationError

@validate_arguments
def GetBooks(q:str) -> object:
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q="+q)
    return r.json()

