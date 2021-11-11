from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas, database, models
from sqlalchemy.orm import Session

from ..hashing import Hash

from ..repository import user

get_db = database.get_db

router = APIRouter(
    prefix="/user",
    tags=['User']

)



@router.post('/')
def create_user(request: schemas.User, db : Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model = schemas.ShowUser)
def get_user(id:int, db : Session = Depends(get_db)):
    return user.get_user(id, db)
