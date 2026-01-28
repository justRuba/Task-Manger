from pydantic import BaseModel, Field, field_validator
from typing import Literal, Optional, Annotated

# ---------- NESTED MODEL ----------
class Profile(BaseModel):
    bio: Annotated[Optional[str], Field(description="User biography", max_length=100)] = None
    website: Optional[str] = None

# ---------- USERS ----------
class User(BaseModel):
    user_id: str
    username: Annotated[str, Field(min_length=3, max_length=20)]
    user_role: Literal["admin", "manager", "team_member"]
    email: str
    profile: Optional[Profile] = None  # Nested Model

# ---------- TASKS ----------
class TaskCreate(BaseModel):
    title: str
    description: str
    status: Literal["todo", "in_progress", "done"]
    priority: Annotated[str, Field(pattern="^(low|medium|high)$")] 
    assign_user: str

    @field_validator('title')
    @classmethod
    def title_must_be_capitalized(cls, v: str) -> str:
        if not v[0].isupper():
            raise ValueError("The first letter of the title must be capitalized!")
        return v

class Task(TaskCreate):
    task_id: str