from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import TaskRequest
from agent import process_task
from database import save_task, get_history

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow everything (for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/run")
def run_task(req: TaskRequest):
    result = process_task(req.task, req.task_type)
    save_task(req.task, result)
    return {"result": result}

@app.get("/history")
def history():
    return get_history()