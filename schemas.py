from pydantic import BaseModel


class PatientCreate(BaseModel):
    name: str
    age: int
    blood_grp: str


class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    blood_grp: str
    model_config ={
        "from_attributes":True
    }
    
class PatientUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    blood_grp: str | None = None
    
class UserCreate(BaseModel):
    name : str
    email:str
    password:str
    
class UserResponse(BaseModel):
    id:int 
    name:str
    email:str
    class Config:
        from_attributes = True 
        
class UserLogin(BaseModel):
    email:str
    password:str