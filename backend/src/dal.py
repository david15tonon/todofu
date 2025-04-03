from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
from pymongo import ReturnDocument
from pydantic import BaseModel

class ListSummary(BaseModel):
    id: str
    name: str
    item_count: int
    