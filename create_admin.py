from sqlmodel import Session
from app.db import engine
from app.models.user import User
from app.services.auth_service import hash_password

print(hash_password("123456"))

with Session(engine) as session:
    admin = User(
        username="zhangpp",
        password_hash=hash_password("123456"),
        role="admin"
    )
    session.add(admin)
    session.commit()
