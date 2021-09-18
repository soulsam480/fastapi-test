from typing import List, Optional
from fastapi import FastAPI
from enum import Enum
from fastapi.params import Query
from pydantic import BaseModel

app = FastAPI()


class ModelName(str, Enum):
    name = "sambit"


class Item(BaseModel):
    name: str
    quantity: int


fake_items_db: List[Item] = []


# root
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/home')
def home():
    return 'You\'ve reached home !'


# query params
@app.get('/query')
def query_params(name: str, email: Optional[str] = ''):
    return {"name": name, "email": email}


# request body
@app.post('/item')
def create_item(item: Item):
    fake_items_db.append(item)
    return fake_items_db


# request validations
@app.get('/validation')
def validate(name: str = Query(..., max_length=5, min_length=2)):
    return name


# params
@app.get('/{name}')
def get_name(name: str):
    return {"name": name}


@app.get('/model/{model_name}')
def model_name(model_name: ModelName):
    return {"name": model_name.value}
