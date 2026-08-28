from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text 
from model import Base,User

DATABASE_URL = "postgresql://adityapandey@localhost/fastapi_learning"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind = engine )

Base.metadata.create_all(bind = engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 
        
