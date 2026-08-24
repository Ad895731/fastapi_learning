from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

from database import SessionLocal
from model import Patient

app = FastAPI()

db = SessionLocal()

# class Patient(BaseModel):
#     name:str
#     age:int 
#     blood_grp:str

# class Doctor(BaseModel):
#     name:str
#     age:int
#     specialization:str
    
class PatientCreate(BaseModel):
    name: str
    age: int
    blood_grp: str


class Patient(PatientCreate):
    id: int
    
# patients = []
    
# @app.get("/")
# def home():
#     return {"message": "FastAPI is working!"}

# @app.get("/hello")
# def print():
#     return {"message": "Hello Aditya"}

# @app.get("/patient/{patient_id}")
# def get_patient(patient_id:int ):
#     return {"message": patient_id}

# @app.get("/doctor/{doctor_id}")
# def get_doctor(doctor_id:int):
#     return {"/doctor_id":doctor_id,
#             "message":"docotr found"}
    
# @app.get("/doctors")
# def get_special(specialization:Optional[str]=None):
#     return {"specialization":specialization}

# @app.post("/patients")
# def create_patients(patient:Patient):
#     ##print(patient)
#      patients.append(patient)
#      return patient

# @app.get("/patients")
# def get_patients():
#     return patients

# @app.post("/doctors")
# def doctor_create(doctor: Doctor):
#     return doctor

@app.post("/patients")
def create_patient(patient:PatientCreate):
    db = SessionLocal()
    new_patient = Patient(
        name=patient.name,
        age=patient.age,
        blood_grp=patient.blood_grp
    )
    db.add(new_patient)
    db.commit(new_patient)
    db.refresh(new_patient)
    
    db.close()
    return new_patient
    # patients.append(new_patient)
    
# @app.get("/patients/{patient_id}")
# def get_patients(patient_id:int):
#     for patient in patients:
#         if(patient_id == patient.id):
#           return patient
#     raise HTTPException(
#     status_code=404,
#     detail="Patient not found"
# )
    
# @app.put("/patients/{patient_id}")
# def update_patient(patient_id: int, updated_patient: PatientCreate):
#     for patient in patients:
#         if patient.id == patient_id:
#             patient.name = updated_patient.name
#             patient.age = updated_patient.age
#             patient.blood_grp = updated_patient.blood_grp
#             return patient
#     raise HTTPException(
#         status_code=404,
#         detail="Patient not found"
#     )
    
# @app.delete("/patients/{patient_id}")
# def get_patients(patient_id:int):
#     for patient in patients:
#         if(patient_id == patient.id):
#           patients.remove(patient)
#           return patient
#     raise HTTPException(
#     status_code=404,
#     detail="Patient not found"
# )