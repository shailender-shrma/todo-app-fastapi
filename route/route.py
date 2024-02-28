from fastapi import APIRouter, WebSocket
from models.todos import Todo
from database.database import collection_name
from schemas.schemas import list_serial, individual_serial
from bson import ObjectId
from fastapi.responses import HTMLResponse


router = APIRouter()


@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos


@router.post("/")
async def create_todo(todo: Todo):
    response = collection_name.insert_one(dict(todo))
    return {"message": "ok this is working"}


@router.put("/{id}")
async def put_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})


@router.websocket("/ws")
async def web_socket(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"message was {data}")
