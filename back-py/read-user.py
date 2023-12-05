# main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"teste": "tudocerto"}


@app.get("/user/{id}")
def read_user(id: int):
    try:
        with open("db.json", "r") as file:
            data = json.load(file)

            for user in data["usuario"]:
                if user["id"] == id:
                    return user

            raise HTTPException(status_code=404, detail="Usuário não encontrado")
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Arquivo db.json não encontrado")

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500, detail="Erro ao decodificar o conteúdo JSON"
        )
