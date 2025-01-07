from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

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
