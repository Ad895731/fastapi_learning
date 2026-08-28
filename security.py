from pwdlib import PasswordHash
import jwt
password_hash = PasswordHash.recommended()

SECRET_KEY = "my-super-secret-key-for-fastapi-learning-2026"
ALGORITHM = "HS256"

def create_access_token ( data : dict ):
   return jwt.encode(
      data, 
      SECRET_KEY,
      algorithm=ALGORITHM
   )

def verify_access_token(token:str):
   try:
      payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
      return payload
   except jwt.InvalidTokenError:
      return None