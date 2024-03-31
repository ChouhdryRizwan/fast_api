from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

app = FastAPI()

@app.get("/")
def home():
    return {"message": "First FastAPI app"}


url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="",
    host="localhost",
    database="mydb",
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()