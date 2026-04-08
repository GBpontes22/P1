from repositories.concessionaria_repository import *

def format_concessionaria(concessionaria):
    concessionaria["_id"] = str(concessionaria["_id"])
    return concessionaria

def create_concessionaria_service(concessionaria):
    result = create_concessionaria(concessionaria.model_dump())
    return {"message": "Veículo criado", "id": str(result.inserted_id)}

def get_all_concessionarias_service():
    concessionarias = get_all_concessionarias()
    return [format_concessionaria(concessionaria) for concessionaria in concessionarias]

def get_concessionaria_by_id_service(concessionaria_id):
    try:
        concessionaria = get_concessionaria_by_id(concessionaria_id)
    except:
        return {"error": "ID inválido"}
    if not concessionaria:
        return {"error": "Veículo não encontrado"}
    return format_concessionaria(concessionaria)

def update_concessionaria_service(concessionaria_id, concessionaria):
    try:
        result = update_concessionaria(concessionaria_id, concessionaria.model_dump())
    except:
        return {"error": "ID inválido"}
    if result.matched_count == 0:
        return {"error": "Veículo não encontrado"}
    return {"message": "Veículo atualizado"}

def delete_concessionaria_service(concessionaria_id):
    try:
        result = delete_concessionaria(concessionaria_id)
    except:
        return {"error": "ID inválido"}
    if result.deleted_count == 0:
        return {"error": "Veículo não encontrado"}
    return {"message": "Veículo removido"}