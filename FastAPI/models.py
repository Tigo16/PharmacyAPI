from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from FastAPI.database import Base

class Drug(Base):
    __tablename__ = "drugs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    dosage = Column(String, nullable=False)
    indications = Column(String, nullable=True)
    contraindications = Column(String, nullable=True)

    inventory = relationship("Inventory", back_populates="drug")


class Pharmacy(Base):
    __tablename__ = "pharmacies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    specialization = Column(String, nullable=True)

    inventory = relationship("Inventory", back_populates="pharmacy")


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    drug_id = Column(Integer, ForeignKey("drugs.id"), nullable=False)
    pharmacy_id = Column(Integer, ForeignKey("pharmacies.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    expiration_date = Column(Date, nullable=False)

    drug = relationship("Drug", back_populates="inventory")
    pharmacy = relationship("Pharmacy", back_populates="inventory")