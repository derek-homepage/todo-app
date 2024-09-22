from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import databases
import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean

# 数据库 URL
DATABASE_URL = "sqlite:///./test.db"

# 数据库
database = databases.Database(DATABASE_URL)

# SQLAlchemy
metadata = sqlalchemy.MetaData()

# 定义表
todos = sqlalchemy.Table(
    "todos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", String),
    Column("completed", Boolean),
)

# 创建引擎
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

app = FastAPI()

# 启用 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Todo(TodoCreate):
    id: int

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/todos/", response_model=Todo)
async def create_todo(todo: TodoCreate):
    query = todos.insert().values(**todo.dict())
    last_record_id = await database.execute(query)
    return {**todo.dict(), "id": last_record_id}

@app.get("/todos/", response_model=List[Todo])
async def read_todos():
    query = todos.select()
    return await database.fetch_all(query)

@app.get("/todos/{todo_id}", response_model=Todo)
async def read_todo(todo_id: int):
    query = todos.select().where(todos.c.id == todo_id)
    todo = await database.fetch_one(query)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo: TodoCreate):
    query = todos.update().where(todos.c.id == todo_id).values(**todo.dict())
    await database.execute(query)
    return {**todo.dict(), "id": todo_id}

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    query = todos.delete().where(todos.c.id == todo_id)
    await database.execute(query)
    return {"message": "Todo deleted successfully"}