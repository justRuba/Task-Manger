from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, tasks
from utils.db_helper import init_db

# Create database tables on startup
init_db()

app = FastAPI(title="Task Manager API (JSON + SQL)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "API is running. Database and JSON systems active."}