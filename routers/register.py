from pwdlib import PasswordHash
from fastapi import APIRouter, HTTPException, Depends
from database import get_db
from model import User as u_m
from schemas import UserCreate, UserResponse

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(user:UserCreate, db = Depends(get_db)):
    existing_user = db.query(u_m).filter(u_m.email==user.email).first()
    if existing_user:
      raise HTTPException(
    status_code=400,
    detail="Email already registered"
    )
    password_hash = PasswordHash.recommended()
    hashed_password = password_hash.hash(user.password)
    new_user = u_m(
    name=user.name,
    email=user.email,
    password_hash=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
