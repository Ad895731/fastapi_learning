from fastapi import APIRouter, HTTPException, Depends
from database import get_db
from model import Patient as p_m
from schemas import PatientCreate, PatientResponse , PatientUpdate

router = APIRouter()

    

@router.post("/patients", response_model = PatientResponse)
def create_patient(patient:PatientCreate, db = Depends(get_db)):
    
    new_patient = p_m(
        name=patient.name,
        age=patient.age,
        blood_grp=patient.blood_grp
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    
    
    return new_patient
    
@router.get("/patients/{patient_id}" , response_model = PatientResponse)
def get_patients(patient_id:int , db = Depends(get_db) ):
    patients = db.query(p_m).all()
    for pd in patients:
        if(patient_id==pd.id):
          return pd
    
@router.delete(("/patients/{patient_id}"))
def delete_patient(patient_id:int, db = Depends(get_db)):
    
    patient = db.query(p_m).filter(p_m.id==patient_id).first()
    if not patient:
        raise HTTPException(status_code=404,
                detail="Patient not found")
    db.delete(patient)
    db.commit()
    
    return {" p de.. su.."}

@router.put("/patients/{patient_id}", response_model=PatientResponse)
def update_patient(
    patient_id: int,
    patient: PatientCreate,
    db=Depends(get_db)
):
    existing_patient = db.query(p_m).filter(
        p_m.id == patient_id
    ).first()

    if not existing_patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    existing_patient.name = patient.name
    existing_patient.age = patient.age
    existing_patient.blood_grp = patient.blood_grp

    db.commit()
    db.refresh(existing_patient)

    return existing_patient


@router.patch("/patients/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id:int , patient :PatientUpdate, db = Depends(get_db)):
    existing_patient = db.query(p_m).filter(

        p_m.id == patient_id

    ).first() 
    if not existing_patient:

        raise HTTPException(

            status_code=404,

            detail="Patient not found"

        )
    if patient.name is not None:
        existing_patient.name = patient.name
    if patient.age is not None:
        existing_patient.age = patient.age
    if patient.blood_grp is not None:
        existing_patient.blood_grp = patient.blood_grp
    db.commit()
    db.refresh(existing_patient)

    return existing_patient




# @router.put("/pa../{p_i}",response_model = PatientResponse)
# def u_p(p_i:int , pa:PatientCreate, db = Depends(get_db)):
    
#     e_p=db.query(p_m).filter(p_m.id==p_i).first()
#     if not e_p:
#         raise HTTPException(status_code=404,
#                 detail="Patient not found")
        
#     e_p.name ="NI"
#     e_p.age=21
#     db.commit()
#     db.refresh(e_p)

    

#     return e_p