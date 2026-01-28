from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./data/task_manager.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"
    user_id = Column(String, primary_key=True, index=True)
    username = Column(String)
    user_role = Column(String)
    email = Column(String)
    # Storing profile info as simple columns for SQLite
    bio = Column(String, nullable=True)
    website = Column(String, nullable=True)

class TaskDB(Base):
    __tablename__ = "tasks"
    task_id = Column(String, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(String)
    priority = Column(String)
    assign_user = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)