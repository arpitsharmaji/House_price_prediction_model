from app.schemas import InputData
from sqlalchemy.orm import Session
from app.database.models_db import Prediction
from fastapi import HTTPException, status
from app import schemas 
from app import router
from app.user.models import usermodel
from fastapi import Depends


def create_task(body:InputData, db:Session,user:usermodel):
    data = body.model_dump()
    new_task = Prediction(area_sqft = data["area_sqft"],
                          bedrooms = data["bedrooms"],
                          bathrooms = data["bathrooms"],
                          age = data["age"],
                          location = data["location"],
                          user_id = user.id
                          )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
    
def get_tasks(db:Session,user:usermodel):
    tasks = db.query(Prediction).filter(user.id == Prediction.user_id).all()
    return tasks


def get_one_task(task_id:int, db:Session):
    task = db.query(Prediction).get(task_id)
    if not task:
        return HTTPException(404, detail='task not found')
    else:
        return task
    
def update_task(body:InputData, task_id:int, db:Session,user:usermodel):
    task = db.query(Prediction).filter(Prediction.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task not found")
    if task.user_id != user.id: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="you are not allowed to updfdate this task!")
      
    body = body.model_dump(exclude_unset=True)
    for feild, values in body.items():
        setattr(task, feild, values)     
        
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return task

def delete_task(task_id:int, db:Session, user:usermodel):
    task = db.query(Prediction).get(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task not found")
    if task.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you are not authorised")
    
    db.delete(task)
    db.commit()
    return None

    
    
    
        
    
    
        
    
    

    
    



    