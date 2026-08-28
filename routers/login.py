from fastapi import APIRouter, HTTPException
from fastapi import Depends
from database import get_db
from model import User as u_m
from security import password_hash, create_access_token, verify_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()
@router.post("/login")
def userlogin(user: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    user_check = db.query(u_m).filter(
        u_m.email == user.username
    ).first()
    if not user_check:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    check = password_hash.verify(
        user.password,
        user_check.password_hash
    )
    if not check:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
        
    access_token = create_access_token(
        {"sub":str(user_check.id)}
    )
    return {
        "access_token": access_token,
        "token_type":"bearer"
    }