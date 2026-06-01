from fastapi import APIRouter, Depends, status
from app import controller
from app.schemas import InputData, taskresponseschema
from app.database.db import get_session
from typing import List
from sqlalchemy.orm import session
from app.helpers import is_authenticated
from app.user.models import usermodel

task_routes = APIRouter(prefix="/tasks")


@task_routes.post("/create", response_model=taskresponseschema,status_code=status.HTTP_201_CREATED)
def create_task(body:InputData, db:session = Depends(get_session),user:usermodel = Depends(is_authenticated)):
    return controller.create_task(body, db, user)

@task_routes.get('/all_tasks',response_model=List[taskresponseschema],status_code=status.HTTP_200_OK)
def get_all_tasks(db:session = Depends(get_session),user:usermodel = Depends(is_authenticated)):
    return controller.get_tasks(db,user)


@task_routes.get('/one_task/{task_id}',response_model=taskresponseschema,status_code=status.HTTP_200_OK)
def get_one_task(task_id:int, db:session = Depends(get_session),user:usermodel = Depends(is_authenticated)):
    return controller.get_one_task(task_id,db)
    
@task_routes.put("/update_task/{task_id}",response_model=taskresponseschema,status_code=status.HTTP_201_CREATED)
def update_task(task_id:int, body:InputData, db:session = Depends(get_session),user:usermodel = Depends(is_authenticated)):
    return controller.update_task(body,task_id,db,user)
    
@task_routes.delete("/delete_task/{task_id}",response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int, db:session = Depends(get_session),user:usermodel = Depends(is_authenticated)):
    return controller.delete_task(task_id, db, user)

## now the task routes have been completed till here now there if you want to add more task routes you can add it here but is is for task routes it is not for user routes.....






