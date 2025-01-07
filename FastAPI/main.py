from fastapi import FastAPI
import uvicorn
from .routers import drugs, pharmacies, inventory
from .database import engine
from . import models

# Создание таблиц, если их еще нет
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Подключение роутеров
app.include_router(drugs.router)
app.include_router(pharmacies.router)
app.include_router(inventory.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pharmacy API"}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Pharmacy API"}
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)