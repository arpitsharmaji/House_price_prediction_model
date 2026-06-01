from fastapi import Request,status,HTTPException,Depends
import jwt
from sqlalchemy.orm import session, Session
from app.user.models import usermodel
from jwt.exceptions import InvalidTokenError
from app.database.settings import setttings
from app.database.db import get_session




def is_authenticated(request:Request, db:Session=Depends(get_session)):
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