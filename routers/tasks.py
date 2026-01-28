from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.models import Task, TaskCreate
from utils.json_helper import read_json, write_json
from utils.db_helper import SessionLocal, TaskDB, UserDB

router = APIRouter(prefix="/tasks", tags=["Tasks"])
TASKS_FILE = "data/tasks.json"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_task_id():
    tasks = read_json(TASKS_FILE)
    if not tasks: return "T001"
    last_id = tasks[-1].get("task_id", "T000")
    num = int(last_id[1:]) + 1
    return f"T{num:03d}"

@router.post("/")
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    # Check if user exists in SQL
    user = db.query(UserDB).filter(UserDB.user_id == task.assign_user).first()
    if not user:
        raise HTTPException(status_code=400, detail="Assigned user not found")

    task_id = generate_task_id()
    task_data = task.model_dump()
    task_data["task_id"] = task_id

    # 1. Save to JSON
    tasks_list = read_json(TASKS_FILE)
    tasks_list.append(task_data)
    write_json(TASKS_FILE, tasks_list)

    # 2. Save to SQLite
    db_task = TaskDB(**task_data)
    db.add(db_task)
    db.commit()

    return {"message": "Task created successfully", "task": task_data}

@router.get("/search_by_user")
async def tasks_by_user(user_id: str, db: Session = Depends(get_db)):
    return db.query(TaskDB).filter(TaskDB.assign_user == user_id).all()

@router.get("/search_user_by_task")
async def user_by_task(task_id: str, db: Session = Depends(get_db)):
    # Using a SQL Join to find the user assigned to a specific task
    result = db.query(UserDB).join(TaskDB, UserDB.user_id == TaskDB.assign_user)\
               .filter(TaskDB.task_id == task_id).first()
    return result if result else {}