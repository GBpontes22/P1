# CRUD de Concessionária com FastAPI e MongoDB

## Requisitos do professor atendidos

* CRUD com FastAPI
* MongoDB
* Docker para servir a aplicação com o banco
* Arquitetura modular
* Entidade diferente de usuário e produto
* Schema com 4 atributos

## Atributos da concessionária

* nome
* cidade
* quantidade_veiculos
* ativa

## Rodar com Docker

```bash
docker compose up --build
```

Acesse:

```bash
http://localhost:8000/docs
```

## Rodar com uvicorn

Suba primeiro o MongoDB:

```bash
docker compose up mongodb
```

Depois rode a API:

```bash
python -m uvicorn main:app --reload
```

Acesse:

```bash
http://127.0.0.1:8000/docs
```

## Exemplo de JSON

```json
{
  "nome": "AutoCar Niterói",
  "cidade": "Niterói",
  "quantidade_veiculos": 120,
  "ativa": true
}
```
