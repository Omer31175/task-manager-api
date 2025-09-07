from fastapi import FastAPI, HTTPException, status, Query
from pydantic import BaseModel, field_validator
from typing import Optional, List
from datetime import datetime, timezone

# ---------------------------------------------------
# Helper function for generating a new ID
# ---------------------------------------------------
def get_new_task_id(current_tasks: List[dict]) -> int:
    return max((t["id"] for t in current_tasks), default=0) + 1

# ---------------------------------------------------
# Pydantic models
# ---------------------------------------------------
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    completed: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Learn FastAPI",
                "completed": False,
                "created_at": "2025-09-03T20:00:00Z",
                "updated_at": "2025-09-03T20:00:00Z"
            }
        }


class TaskCreate(BaseModel):
    title: str
    completed: bool = False

    @field_validator("title")
    def title_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("Title must not be empty")
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Complete portfolio project",
                "completed": False
            }
        }


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

    @field_validator("title")
    def title_must_not_be_blank(cls, v):
        if v is not None and not v.strip():
            raise ValueError("Title must not be empty")
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Finish FastAPI project",
                "completed": True
            }
        }


class MessageResponse(BaseModel):
    message: str

# ---------------------------------------------------
# In-memory storage (for demo only)
# ---------------------------------------------------
tasks = [
    {
        "id": 1,
        "title": "Buy groceries",
        "completed": False,
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc)
    },
    {
        "id": 2,
        "title": "Finish FastAPI project",
        "completed": True,
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc)
    },
    {
        "id": 3,
        "title": "Call client",
        "completed": False,
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc)
    }
]

# ---------------------------------------------------
# FastAPI app
# ---------------------------------------------------
app = FastAPI(
    title="Portfolio Task Manager API",
    description=(
        "A simple task management API built with FastAPI, "
        "demonstrating CRUD operations, timestamps, and data validation."
    ),
    version="1.2.0"
)

# ---------------------------------------------------
# Endpoints
# ---------------------------------------------------

@app.get("/tasks", response_model=List[Task], tags=["Tasks"])
def list_tasks(completed: Optional[bool] = Query(None, description="Filter tasks by completion status")):
    """
    Get all tasks.  
    Optionally filter by `completed=true` or `completed=false`.
    """
    filtered = tasks if completed is None else [t for t in tasks if t["completed"] == completed]
    return [Task(**t) for t in filtered]


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["Tasks"])
def create_task(task_data: TaskCreate):
    """
    Create a new task.  
    Titles must be unique (case-insensitive).
    """
    title_normalized = task_data.title.strip().lower()
    if any(t["title"].strip().lower() == title_normalized for t in tasks):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task with this title already exists"
        )

    new_id = get_new_task_id(tasks)
    now = datetime.now(timezone.utc)
    new_task = Task(
        id=new_id,
        title=task_data.title,
        completed=task_data.completed,
        created_at=now,
        updated_at=now
    )
    tasks.append(new_task.model_dump())
    return new_task


@app.patch("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def update_task(task_id: int, updated_data: TaskUpdate):
    """
    Update an existing task.  
    Supports partial updates (title or completed).
    """
    for task in tasks:
        if task["id"] == task_id:
            # Check duplicate title
            if updated_data.title is not None:
                title_normalized = updated_data.title.strip().lower()
                if any(
                    t["title"].strip().lower() == title_normalized and t["id"] != task_id
                    for t in tasks
                ):
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Task with this title already exists"
                    )

            update_data = updated_data.model_dump(exclude_unset=True)
            task.update(update_data)
            task["updated_at"] = datetime.now(timezone.utc)
            return Task(**task)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )


@app.delete("/tasks/{task_id}", response_model=MessageResponse, tags=["Tasks"])
def delete_task(task_id: int):
    """
    Delete a task by ID.
    """
    found_task = next((t for t in tasks if t["id"] == task_id), None)
    if found_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    tasks.remove(found_task)
    return MessageResponse(message="Task deleted successfully")
