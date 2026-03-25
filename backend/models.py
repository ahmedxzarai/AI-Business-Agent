from pydantic import BaseModel

class TaskRequest(BaseModel):
    task: str
    task_type: str = "general"