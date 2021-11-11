from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas, database, models
from sqlalchemy.orm import Session



def get_all(db : Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog    


def destroy(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'blog with this the if of {id} was not found')
        
    
    blog.delete(synchronize_session=False)

    db.commit()

    return 'done' 


def update(id, request, db: Session):
    # db.query(models.Blog).filter(models.Blog.id == id).update(request) in chera error mide?

    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'blog with this the if of {id} was not found')
        
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return 'updated'



def show(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'blog with this the if of {id} was not found')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'datail' : f'blog with this the if of {id} was not found'}
    return blog 