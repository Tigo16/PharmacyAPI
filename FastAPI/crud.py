from sqlalchemy.orm import Session
from FastAPI import models, schemas

# CRUD для Drug
def create_drug(db: Session, drug: schemas.DrugCreate):
    db_drug = models.Drug(**drug.dict())
    db.add(db_drug)
    db.commit()
    db.refresh(db_drug)
    return db_drug

def get_drugs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Drug).offset(skip).limit(limit).all()

def update_drug(db: Session, drug_id: int, drug: schemas.DrugCreate):
    db_drug = db.query(models.Drug).filter(models.Drug.id == drug_id).first()
    if db_drug:
        for key, value in drug.dict().items():
            setattr(db_drug, key, value)
        db.commit()
        db.refresh(db_drug)
    return db_drug

def delete_drug(db: Session, drug_id: int):
    db_drug = db.query(models.Drug).filter(models.Drug.id == drug_id).first()
    if db_drug:
        db.delete(db_drug)
        db.commit()
    return db_drug

# CRUD для Pharmacy
def create_pharmacy(db: Session, pharmacy: schemas.PharmacyCreate):
    db_pharmacy = models.Pharmacy(**pharmacy.dict())
    db.add(db_pharmacy)
    db.commit()
    db.refresh(db_pharmacy)
    return db_pharmacy

def get_pharmacies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Pharmacy).offset(skip).limit(limit).all()

def update_pharmacy(db: Session, pharmacy_id: int, pharmacy: schemas.PharmacyCreate):
    db_pharmacy = db.query(models.Pharmacy).filter(models.Pharmacy.id == pharmacy_id).first()
    if db_pharmacy:
        for key, value in pharmacy.dict().items():
            setattr(db_pharmacy, key, value)
        db.commit()
        db.refresh(db_pharmacy)
    return db_pharmacy

def delete_pharmacy(db: Session, pharmacy_id: int):
    db_pharmacy = db.query(models.Pharmacy).filter(models.Pharmacy.id == pharmacy_id).first()
    if db_pharmacy:
        db.delete(db_pharmacy)
        db.commit()
    return db_pharmacy

# CRUD для Inventory
def create_inventory(db: Session, inventory: schemas.InventoryCreate):
    db_inventory = models.Inventory(**inventory.dict())
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

def get_inventory(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Inventory).offset(skip).limit(limit).all()

def update_inventory(db: Session, inventory_id: int, inventory: schemas.InventoryCreate):
    db_inventory = db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()
    if db_inventory:
        for key, value in inventory.dict().items():
            setattr(db_inventory, key, value)
        db.commit()
        db.refresh(db_inventory)
    return db_inventory

def delete_inventory(db: Session, inventory_id: int):
    db_inventory = db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()
    if db_inventory:
        db.delete(db_inventory)
        db.commit()
    return db_inventory