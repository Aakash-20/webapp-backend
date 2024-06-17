from fastapi import FastAPI
from . import schemas, models
from .database import engine, get_db
import psycopg2

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Jai Shree Ganesh"}



