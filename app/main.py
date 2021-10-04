from fastapi import FastAPI, APIRouter
import uvicorn
from dotenv import load_dotenv
load_dotenv()
from app.Routes import BookRoute



app = FastAPI(title="Book API",openapi_url="/openapi.json")

app.include_router(BookRoute.router)




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")

