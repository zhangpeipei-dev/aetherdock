from sqlmodel import Session, select
from app.models.user import User

def get_user_by_name(session: Session, username: str) -> User:
    statement = select(User).where(User.username == username)
    result = session.exec(statement).first()
    return result

def create_user(session: Session, user: User) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user