from fastapi import FastAPI, Body, Query
from typing import Optional

from models.person import Person
app = FastAPI()

@app.get('/')
def home():
    return {'from': 'FastAPI'}

@app.post('/person/new')
def create_person(person: Person = Body(...)):
    return person
    #esos ... es para marcar que es requerido

#Revisar la doc, porque ha cambiado un poco
@app.get('/detail',description="The description the method that looks for a person")
def get_detail(
    name: Optional[str] = Query(min_length=0, max_length=50, description="search using the name", default=None),
    age: int = Query(...)
):
    return {name: age}