from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    is_active: bool = True
    is_admin: bool = False


class UserInDB(BaseModel):
    id: int
    props: dict

    class Config:
        orm_mode = True
        load_instance = True
