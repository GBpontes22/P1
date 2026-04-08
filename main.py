from fastapi import FastAPI
from routers.concessionaria_router import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"Message": "Sistema de cadastro de concessionaria com MongoDB e FastAPI"}