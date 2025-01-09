from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from FastAPI import crud, schemas
from FastAPI.database import get_db
from FastAPI.schemas import Pagination

router = APIRouter(prefix="/pharmacies", tags=["Pharmacies"])

@router.post("/", response_model=schemas.Pharmacy)
def create_pharmacy(pharmacy: schemas.PharmacyCreate, db: Session = Depends(get_db)):
    return crud.create_pharmacy(db=db, pharmacy=pharmacy)

@router.get("/", response_model=Pagination[schemas.Pharmacy])
def read_pharmacies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    total_count = db.query(Pharmacy).count()  # Get the total number of records
    pharmacies = crud.get_pharmacies(db=db, skip=skip, limit=limit)
    return {"items": pharmacies, "total_count": total_count}

@router.put("/{pharmacy_id}", response_model=schemas.Pharmacy)
def update_pharmacy(pharmacy_id: int, pharmacy: schemas.PharmacyCreate, db: Session = Depends(get_db)):
    db_pharmacy = crud.update_pharmacy(db=db, pharmacy_id=pharmacy_id, pharmacy=pharmacy)
    if not db_pharmacy:
        raise HTTPException(status_code=404, detail="Pharmacy not found")
    return db_pharmacy

@router.delete("/{pharmacy_id}")
def delete_pharmacy(pharmacy_id: int, db: Session = Depends(get_db)):
    db_pharmacy = crud.delete_pharmacy(db=db, pharmacy_id=pharmacy_id)
    if not db_pharmacy:
        raise HTTPException(status_code=404, detail="Pharmacy not found")
    return {"message": "Pharmacy deleted successfully"}