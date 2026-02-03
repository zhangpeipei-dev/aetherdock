from fastapi import Depends, HTTPException, Header
from sqlmodel import Session
from app.db import get_session
from app.core.security import decode_access_token
from app.repository.user_repo import get_user_by_name

def get_db(session: Session = Depends(get_session)) -> Session:
    return session

def get_current_user(
    authorization: str = Header(...),
    session: Session = Depends(get_session)
):
    token = authorization.replace("Bearer ", "")
    payload = decode_access_token(token)
    username = payload.get("sub")
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = get_user_by_name(session, username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

def require_admin(user: User = Depends(get_current_user)):
    return user
