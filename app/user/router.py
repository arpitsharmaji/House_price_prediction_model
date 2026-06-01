from fastapi import APIRouter, Depends, status, Response, Request
from app.user import controller
from sqlalchemy.orm import Session
from app.user.dtos import UserSchema, UserResponseSchema, LoginSchema
from app.database.db import get_session
from app.user.models import usermodel


user_routes = APIRouter(prefix="/user")

@user_routes.post("/register",response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED )
def register_user(body:UserSchema, db:Session = Depends(get_session)):
    return controller.register_user(body, db)

@user_routes.post("/login_user",status_code=status.HTTP_200_OK)
def login(body:LoginSchema, db:Session = Depends(get_session)):
    return controller.login_user(body,db)

@user_routes.get("/is_auth",response_model=UserResponseSchema,status_code=status.HTTP_200_OK)
def is_auth(request:Request, db:Session = Depends(get_session)):
    return controller.is_authenticated(request, db)
 


    
    
