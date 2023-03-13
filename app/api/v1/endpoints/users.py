from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from app.core.config import settings

from app.scheme import Token, User
from app.tools import authenticate_user, create_access_token
from app.tools.secure import get_current_admin_user
from app.models import User as UserModel

users_router = APIRouter(prefix="/users")


@users_router.post("/", status_code=200, response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.props["username"]},
        expires_delta=access_token_expires,
    )
    return Token.parse_obj({"access_token": access_token, "token_type": "bearer"})


@users_router.get("/", status_code=200, response_model=list[User])
async def list_(user: User = Depends(get_current_admin_user)) -> list[User]:
    return UserModel.all()
