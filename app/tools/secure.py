from datetime import timedelta, datetime, timezone

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from starlette import status

from app.core.config import settings
from app.scheme import TokenData, UserInDB
from app.models import User as UserModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(username: str):
    if user := UserModel.get_by_username(username):
        return UserInDB.from_orm(user)
    return False


def authenticate_user(username: str, password: str):
    if user := get_user(username):
        return (
            user if verify_password(password, user.props["hashed_password"]) else False
        )
    else:
        return False


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode["exp"] = expire
    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ACCESS_TOKEN_ALGORITHM,
    )


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ACCESS_TOKEN_ALGORITHM],
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError as e:
        raise credentials_exception from e

    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


def get_current_admin_user(current_user: UserInDB = Depends(get_current_user)):
    if not current_user.props["is_admin"]:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
