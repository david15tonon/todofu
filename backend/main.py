from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
#Model
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


#Endpoints
def read_root():
    return {"Hello":"World"}


@app.put("/items/{item_id}")
def read_item(item_id:int, item:Item):
    return {"item_nme": item.name,"item_id": item_id}
