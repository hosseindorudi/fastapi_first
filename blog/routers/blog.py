from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session

from ..repository import blog



get_db = database.get_db

router = APIRouter(
    prefix="/blog",
    tags=['Blog']

)



@router.get('/', response_model = List[schemas.ShowBlog])
def get_all_blog(db : Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)) :
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request : schemas.Blog, db : Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)



@router.get('/{id}', status_code = 200, response_model = schemas.ShowBlog)
def get_one_blog(id:int, db : Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int, request : schemas.Blog, db : Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)




@router.delete('/blog/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db : Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)
