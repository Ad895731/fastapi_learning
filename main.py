from fastapi import FastAPI
from routers import patients
from routers import register
from routers import login
from typing import Optional
from database import SessionLocal
from model import Patient as p_m
from security import password_hash,create_access_token,verify_access_token
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from model import User as u_m
from database import get_db
from schemas import UserResponse

app = FastAPI()
app.include_router(patients.router)
app.include_router(register.router)
app.include_router(login.router)

