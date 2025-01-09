from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from FastAPI import crud, schemas
from FastAPI.database import get_db
from FastAPI.models import Drug
from FastAPI.schemas import Pagination

router = APIRouter(prefix="/drugs", tags=["Drugs"])

@router.post("/", response_model=schemas.Drug)
def create_drug(drug: schemas.DrugCreate, db: Session = Depends(get_db)):
    return crud.create_drug(db=db, drug=drug)

@router.get("/", response_model=Pagination[schemas.Drug])
def read_drugs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    total_count = db.query(Drug).count()  # Get the total number of records
    drugs = crud.get_drugs(db=db, skip=skip, limit=limit)
    return {"items": drugs, "total_count": total_count}

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

# Filter
@router.get("/filter")
def filter_drugs(
    manufacturer: str,
    min_dosage: str,
    indication: str,
    db: Session = Depends(get_db),
):
    query = db.query(Drug).filter(
        Drug.manufacturer == manufacturer,
        Drug.dosage.ilike(f"%{min_dosage}%"),
        Drug.indications.ilike(f"%{indication}%"),
    )
    return query.all()

# Sorting
@router.get("/drugs/sort")
def get_sorted_drugs(order_by: str = "asc", db: Session = Depends(get_db)):
    query = db.query(Drug)
    if order_by == "asc":
        query = query.order_by(Drug.price.asc())
    elif order_by == "desc":
        query = query.order_by(Drug.price.desc())
    else:
        return {"error": "Invalid order_by value. Use 'asc' or 'desc'."}
    return query.all()