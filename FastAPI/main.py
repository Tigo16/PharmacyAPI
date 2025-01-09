from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import SQLAlchemyError
from FastAPI.routers import drugs, pharmacies, inventory
from FastAPI.database import engine, Base

try:
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully.")
except SQLAlchemyError as e:
    print(f"Error initializing database: {e}")

app = FastAPI(
    title="Pharmacy API",
    description="API для управления аптеками и наличием лекарств",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(drugs.router, prefix="/drugs", tags=["Drugs"])
app.include_router(pharmacies.router, prefix="/pharmacies", tags=["Pharmacies"])
app.include_router(inventory.router, prefix="/inventory", tags=["Inventory"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Pharmacy API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
