from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from FastAPI import crud, schemas
from FastAPI.database import get_db
from FastAPI.models import Inventory, Pharmacy, Drug

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.post("/", response_model=schemas.Inventory)
def create_inventory(inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    return crud.create_inventory(db=db, inventory=inventory)

@router.get("/", response_model=list[schemas.Inventory])
def read_inventory(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_inventory(db=db, skip=skip, limit=limit)

@router.put("/{inventory_id}", response_model=schemas.Inventory)
def update_inventory(inventory_id: int, inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    db_inventory = crud.update_inventory(db=db, inventory_id=inventory_id, inventory=inventory)
    if not db_inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return db_inventory

@router.delete("/{inventory_id}")
def delete_inventory(inventory_id: int, db: Session = Depends(get_db)):
    db_inventory = crud.delete_inventory(db=db, inventory_id=inventory_id)
    if not db_inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return {"message": "Inventory deleted successfully"}

#Join
@router.get("/inventory/expiring")
def get_expiring_inventory(expiration_date: str, db: Session = Depends(get_db)):
    return db.query(
        Pharmacy.name.label("pharmacy_name"),
        Drug.name.label("drug_name"),
        Inventory.expiration_date,
    ).join(Drug, Inventory.drug_id == Drug.id).join(
        Pharmacy, Inventory.pharmacy_id == Pharmacy.id
    ).filter(
        Inventory.expiration_date < expiration_date
    ).all()

#Update
@router.put("/inventory/update-prices/{pharmacy_id}")
def update_prices(pharmacy_id: int, db: Session = Depends(get_db)):
    subquery = db.query(
        func.avg(Inventory.price).label("avg_price")
    ).filter(Inventory.pharmacy_id == pharmacy_id).scalar()

    db.query(Inventory).filter(
        Inventory.pharmacy_id == pharmacy_id,
        Inventory.price < subquery,
    ).update({"price": Inventory.price * 1.1}, synchronize_session=False)

    db.commit()
    return {"message": "Prices updated successfully"}

#Group by
@router.get("/inventory/statistics")
def get_inventory_statistics(db: Session = Depends(get_db)):
    return db.query(
        Inventory.pharmacy_id,
        func.count(Inventory.id).label("total_drugs"),
        func.avg(Inventory.price).label("average_price"),
    ).group_by(Inventory.pharmacy_id).all()
