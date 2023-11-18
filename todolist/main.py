# create a fastapi application named todo list that will manage a simple todo list. create endpoints for:
#1. grab all todos
#2. grab a single todo by id
#3. create a todo and store it in a dictionary
#4. update a todo
#5. delete a todo

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

app = FastAPI()

class Todo(BaseModel): # used for data validation
    name: str
    due_date: str
    priority: int

todos = {
    1: Todo(name="Kupi karte za utakmicu Istra - Hajduk", due_date="today", priority=1),
    2: Todo( name="Idi na utakmicu Istra - Hajduk", due_date="today", priority=1)
}

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs/") # napravi redirect na docs, da nije prazan browser

@app.get("/todos")
async def get_todos():
    return todos

@app.get("/todos/{todo_id}") 
async def get_todo_by_id(todo_id: int): 
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]

@app.post("/todos")
async def create_a_todo(todo: Todo):
    todo_id = max(todos.keys()) + 1
    todos[todo_id] = todo
    return todos[todo_id]


@app.put("/todos/{todo_id}")
async def update_a_todo_by_id(todo_id: int, todo: Todo):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos[todo_id] = todo
    return todos[todo_id]

@app.delete("/todos/{todo_id}")
async def delete_a_todo_by_id(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
    return {"ok": True}

# run in terminal with:
# uvicorn main:app --reload
# check the url in the terminal and open it in the browser
