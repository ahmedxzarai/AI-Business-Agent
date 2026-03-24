from fastapi import FastAPI
from pydantic import BaseModel
from agent import process_task

app = FastAPI()

class TaskRequest(BaseModel):
    task: str

@app.post("/run")
def run_task(req: TaskRequest):
    result = process_task(req.task)
    return {"result": result}