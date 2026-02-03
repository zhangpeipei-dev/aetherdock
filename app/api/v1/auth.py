from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.user import UserLogin, UserRead
from app.services.auth_service import login
from app.api.deps import get_current_user, get_db
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def user_login(
    data: UserLogin,
    session: Session = Depends(get_db)
):
    token = login(session, data.username, data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UserRead)
def get_current_user_info(
    user: User = Depends(get_current_user)
):
    return user


