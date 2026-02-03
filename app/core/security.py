
from datetime import datetime, timedelta
import hashlib
from venv import logger
import bcrypt
from jose import jwt
from app.core.config import settings

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    
    To support passwords longer than 72 bytes (bcrypt's limit) and to avoid 
    potential issues with passlib+bcrypt compatibility, we first hash the 
    password using SHA256, then hash the result with bcrypt.
    """
    # 1. SHA256 pre-hashing
    # encode to bytes -> sha256 -> hexdigest (str, 64 chars) -> encode to bytes
    password_sha = hashlib.sha256(password.encode('utf-8')).hexdigest().encode('utf-8')
    
    # 2. Bcrypt hashing
    # bcrypt.hashpw returns bytes, we decode to str for storage
    hashed = bcrypt.hashpw(password_sha, bcrypt.gensalt())
    return hashed.decode('utf-8')

def verify_password(plain_password: str, password_hash: str) -> bool:
    """
    Verify a password against a hash.
    """
    try:
        logger.info(f"plain_password: {plain_password}")
        logger.info(f"password_hash: {password_hash}")
        # 1. Apply same SHA256 pre-hashing
        password_sha = hashlib.sha256(plain_password.encode('utf-8')).hexdigest().encode('utf-8')
        
        # 2. Verify with bcrypt
        # bcrypt.checkpw expects bytes for both args
        logger.info(f"password_sha: {password_sha}")
        logger.info(f"password_hash: {password_hash.encode('utf-8')}")
        return bcrypt.checkpw(password_sha, password_hash.encode('utf-8'))
    except (ValueError, TypeError):
        return False

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except jwt.JWTError:
        return {}
