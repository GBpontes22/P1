from fastapi import APIRouter
from schemas.concessionaria_schema import Concessionaria
from services.concessionaria_service import *

router = APIRouter()

@router.get("/concessionaria")
def list_concessionarias():
    return get_all_concessionarias_service()

@router.post("/concessionaria")
def create_concessionaria(concessionaria: Concessionaria):
    return create_concessionaria_service(concessionaria)

@router.get("/concessionaria/{concessionaria_id}")
def get_concessionaria(concessionaria_id: str):
    return get_concessionaria_by_id_service(concessionaria_id)

@router.put("/concessionaria/{concessionaria_id}")
def update_concessionaria(concessionaria_id: str, concessionaria: Concessionaria):
    return update_concessionaria_service(concessionaria_id, concessionaria)

@router.delete("/concessionaria/{concessionaria_id}")
def delete_concessionaria(concessionaria_id: str):
    return delete_concessionaria_service(concessionaria_id)