from fastapi import FastAPI, Body, Query, Path, status, Form, Cookie, Header, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import SecretStr, EmailStr
import aiofiles
import os
import logging

from models.person import Person, Login
from models.location import Localization
app = FastAPI()

@app.get('/')
def home():
    return {'from': 'FastAPI'}

@app.post('/person/new', response_model=Person,response_model_exclude={'password', 'age'}, status_code=status.HTTP_201_CREATED)
def create_person(person: Person = Body(...)):
    return person
    #esos ... es para marcar que es requerido

#Revisar la doc, porque ha cambiado un poco
@app.get('/detail')
def get_detail(
    name: Optional[str] = Query(
        min_length=0,
        max_length=50, 
        description="search using the name",
        title="Name of the person", 
        default=None,
        example="pepe"),
    age: int = Query(...,example=26)
):
    '''
    Getting detailed information

    Using query and path parameters you can find what you were looking for

    Parameters 
    - name
    - age 
    are used for this endpoint

    It will return the name and the age that you entered
    '''
    return {name: age}

persons = [1,2,3,4,5]
@app.get('/person/detail/{person_id}')
def get_person(
    person_id: int = Path(
        ...,
        description="Path parameter to differenciate users",
        gt=0,
        example=1
    )
):
    if person_id not in persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The person was not found"
        )
    return {person_id: 'It works'}

@app.put('/person/update/{person_id}')
def update_person(
    person_id: int = Path(
        ...,
        description="user's id",
        gt=0
    ),
    person: Person = Body(...),
    location: Localization = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results

@app.post(path='/login', response_model=Login)
def login(username: str = Form(...), password: SecretStr = Form(...)):
    return Login(username=username, password=password)

@app.post(path='/contact')
def contact(
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None),
    username: str = Form(...), 
    password: SecretStr = Form(...),
    email: EmailStr = Form(...)
):
    return user_agent


@app.post("/upload_file/", response_description="", response_model = "")
async def upload_file(file:UploadFile = File(...)):
    try:
        print(file.filename)
        async with aiofiles.open(os.path.join('./files/documents', file.filename), 'wb') as out_file:
            content = await file.read()  # async read
            await out_file.write(content)  # async write

    except Exception as e:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = { 'message' : str(e) }
            )
    else:
        return JSONResponse(
            status_code = status.HTTP_200_OK,
            content = {"result":'success'}
            )

@app.post("/upload_image/", response_description="", response_model = "")
async def upload_image(file:UploadFile = File(...)):
    try:
        print(file.filename)
        async with aiofiles.open(os.path.join('./files/images', file.filename), 'wb') as out_file:
            content = await file.read()  # async read
            await out_file.write(content)  # async write

    except Exception as e:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = { 'message' : str(e) }
            )
    else:
        return JSONResponse(
            status_code = status.HTTP_200_OK,
            content = {"result":'success'}
            )