from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Characteristic(BaseModel):
    ram_memory: int
    rom_memory: int

class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic


phones_db: List[Phone] = []


@app.get("/health")
def health_check():
    return "Ok"


@app.post("/phones", status_code=status.HTTP_201_CREATED)
def create_phones(new_phones: List[Phone]):
    global phones_db
    phones_db.extend(new_phones)
    return {"message": f"{len(new_phones)} phone ajouté"}


@app.get("/phones", response_model=List[Phone])
def get_phones():
    return phones_db


@app.get("/phones/{id}", response_model=Phone)
def get_phone(id: str):
    for phone in phones_db:
        if phone.identifier == id:
            return phone
    raise HTTPException(
        status_code=404,detail=f"Phone avec l'identifiant '{id}' n'existe pas."
    )