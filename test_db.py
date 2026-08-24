from database import SessionLocal
from model import Patient
 
db = SessionLocal()
patient = Patient(
    name = "Rahul",
    age = 21 ,
    blood_grp = "A+"
)
db.add(patient)
db.commit()
print("pa.. ad.. succ..")
db.close()