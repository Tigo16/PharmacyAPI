from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/drugs", tags=["Drugs"])

@router.post("/", response_model=schemas.Drug)
def create_drug(drug: schemas.DrugCreate, db: Session = Depends(get_db)):
    return crud.create_drug(db=db, drug=drug)

@router.get("/", response_model=list[schemas.Drug])
def read_drugs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_drugs(db=db, skip=skip, limit=limit)

@router.put("/{drug_id}", response_model=schemas.Drug)
def update_drug(drug_id: int, drug: schemas.DrugCreate, db: Session = Depends(get_db)):
    db_drug = crud.update_drug(db=db, drug_id=drug_id, drug=drug)
    if not db_drug:
        raise HTTPException(status_code=404, detail="Drug not found")
    return db_drug

@router.delete("/{drug_id}")
def delete_drug(drug_id: int, db: Session = Depends(get_db)):
    db_drug = crud.delete_drug(db=db, drug_id=drug_id)
    if not db_drug:
        raise HTTPException(status_code=404, detail="Drug not found")
    return {"message": "Drug deleted successfully"}
