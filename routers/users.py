from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.models import User
from utils.json_helper import read_json, write_json
from utils.db_helper import SessionLocal, UserDB

router = APIRouter(prefix="/users", tags=["Users"])
USERS_FILE = "data/users.json"

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/")
async def create_user(user: User, db: Session = Depends(get_db)):
    # 1. JSON Save
    users_list = read_json(USERS_FILE)
    if any(u["user_id"] == user.user_id for u in users_list):
        raise HTTPException(status_code=400, detail="User ID already exists")
    users_list.append(user.model_dump())
    write_json(USERS_FILE, users_list)

    # 2. SQLite Save (Flattening the Profile for SQL)
    user_data = user.model_dump()
    profile_data = user_data.pop("profile") or {}
    
    db_user = UserDB(
        **user_data,
        bio=profile_data.get("bio"),
        website=profile_data.get("website")
    )
    db.add(db_user)
    db.commit()
    return {"message": "User created with Profile", "user": user.model_dump()}