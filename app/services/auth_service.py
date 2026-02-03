from sqlmodel import Session
from app.core.security import hash_password, verify_password, create_access_token
from app.repository.user_repo import get_user_by_name
from app.core.logging import logger

def authenticate_user(session: Session, username: str, password: str):
    user = get_user_by_name(session, username)
    # logger.info(f"find user: {user}")
    if not user:
        logger.info(f"user not found")
        return None
    if not verify_password(password, user.password_hash):
        logger.info(f"find user but verify_password failed")
        return None
    logger.info(f"authenticate_user success")
    return user
    

def login(session: Session, username: str, password: str) -> str:
    user = authenticate_user(session, username, password)
    if not user:
        return ""
    access_token = create_access_token({"sub": user.username})
    return access_token