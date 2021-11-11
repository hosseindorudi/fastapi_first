from fastapi import FastAPI, Depends, status, Response, HTTPException
from typing import List
from . import schemas, models
from .database import engine, SessionLocal

from sqlalchemy.orm import Session

from .hashing import Hash

from .routers import blog, user, authentication
from .database import get_db

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

# @app.post('/blog')
# def create(title, body):
#     return f'created - {title} - {body}'.format(title=title, body=body)






# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blog'])
# def create(request : schemas.Blog, db : Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.get('/blog', response_model = List[schemas.ShowBlog], tags=['blog'])
# def get_all_blog(db : Session = Depends(get_db)) :
#     blogs = db.query(models.Blog).all()
#     return blogs


# @app.get('/blog/{id}', status_code = 200, response_model = schemas.ShowBlog, tags=['blog'])
# def get_one_blog(id, response : Response, db : Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'blog with this the if of {id} was not found')
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'datail' : f'blog with this the if of {id} was not found'}
#     return blog 

# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blog'])
# def update_blog(id, request : schemas.Blog, db : Session = Depends(get_db)):
#     # db.query(models.Blog).filter(models.Blog.id == id).update(request) in chera error mide?

#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'blog with this the if of {id} was not found')
        
#     blog.update({'title': request.title, 'body': request.body})
#     db.commit()
#     return 'updated'




# @app.delete('/blog/{id}', status_code = status.HTTP_204_NO_CONTENT, tags=['blog'])
# def delete_blog(id, db : Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'blog with this the if of {id} was not found')
        
    
#     blog.delete(synchronize_session=False)

#     db.commit()

#     return 'done' 


# @app.post('/user', tags=['user'])
# def create_user(request: schemas.User, db : Session = Depends(get_db)):
#     new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get('/user/{id}', response_model = schemas.ShowUser, tags=['user'])
# def get_user(id:int, db : Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
    
#     if not user:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'user with this the if of {id} was not found')

#     return user    
