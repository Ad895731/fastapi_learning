from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column , Integer , String 
class Base(DeclarativeBase):
    pass

class Patient(Base):
    __tablename__ ="patients"
    
    id = Column(Integer , primary_key = True)
    name = Column(String (100))
    age = Column(Integer)
    blood_grp= Column(String(10))
    
class User(Base):
    __tablename__="users"
    
    id = Column(Integer,primary_key=True)
    name = Column(String(100))
    email=Column(String(150), unique =True)
    password_hash = Column(String(255))