from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text 
from model import Base

DATABASE_URL = "postgresql://adityapandey@localhost/fastapi_learning"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind = engine )
db = SessionLocal()

Base.metadata.create_all(bind = engine)
