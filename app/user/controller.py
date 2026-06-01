from app.user.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import session, Session
from app.user.models import usermodel
from fastapi import HTTPException, status, Request
from pwdlib import PasswordHash
import jwt
from jwt.exceptions import InvalidTokenError
from app.database.settings import setttings
from datetime import datetime, timedelta

password_hash = PasswordHash.recommended()

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def register_user(body:UserSchema,db:Session):
    is_user = db.query(usermodel).filter(usermodel.username == body.username).first()
    if is_user:
        raise HTTPException(400, detail='username already exist..')
    is_email = db.query(usermodel).filter(usermodel.email == body.email).first()
    if is_email:
        raise HTTPException(400, 'email already exist...')
    
    hash_password = get_password_hash(body.password)
    new_user = usermodel(
        name = body.name,
        username = body.username,
        hash_password = hash_password,
        email = body.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
    
def get_password_hash(password):
    return password_hash.hash(password)

def login_user(body:LoginSchema, db:Session):
    user = db.query(usermodel).filter(usermodel.username == body.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "user does not exist")
    password = verify_password(body.password, user.hash_password)
    if not password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "password not matched")
    exp_time = datetime.now() + timedelta(minutes=setttings.EXP_TIME)
    token = jwt.encode({"_id":user.id, "exp":exp_time}, setttings.SECRET_KEY, setttings.ALGORITHM)
    return {'token':token}

def is_authenticated(request:Request, db:Session):
    try:
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        token = token.split(" ")[-1].strip('"')
        data = jwt.decode(token,setttings.SECRET_KEY,algorithms=[setttings.ALGORITHM])
        user = db.query(usermodel).filter(data.get('_id') == usermodel.id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
        
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
