from pydantic import BaseModel
from typing import Optional, TypeVar, Generic, List
from datetime import date

T = TypeVar('T')

class Pagination(BaseModel, Generic[T]):
    total: int
    items: List[T]

class DrugBase(BaseModel):
    name: str
    manufacturer: str
    dosage: str
    indications: Optional[str] = None
    contraindications: Optional[str] = None

class DrugCreate(DrugBase):
    pass

class Drug(DrugBase):
    id: int

    class Config:
        from_attributes = True


class PharmacyBase(BaseModel):
    name: str
    address: str
    phone: str
    specialization: Optional[str] = None

class PharmacyCreate(PharmacyBase):
    pass

class Pharmacy(PharmacyBase):
    id: int

    class Config:
        from_attributes = True


class InventoryBase(BaseModel):
    drug_id: int
    pharmacy_id: int
    quantity: int
    price: float
    expiration_date: date

class InventoryCreate(InventoryBase):
    pass

class Inventory(InventoryBase):
    id: int

    class Config:
        from_attributes = True