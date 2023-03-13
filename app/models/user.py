from __future__ import annotations
from sqlalchemy import Column, Integer, Unicode
from sqlalchemy.dialects.postgresql import JSONB

from .database import Base, SessionLocal
from ..scheme import User as UserScheme


class User(Base):
    __tablename__ = "user"
    id = Column("id", Integer, primary_key=True)
    props = Column("props", JSONB)

    def __init__(self, id, props):
        self.id = id
        self.props = props

    @classmethod
    def get_by_username(cls, username) -> User:
        db = SessionLocal()
        return (
            db.query(cls)
            .filter(cls.props["username"].astext.cast(Unicode) == username)
            .first()
        )

    @classmethod
    def all(cls) -> list[UserScheme]:
        db = SessionLocal()
        return [UserScheme.parse_obj(el.props) for el in db.query(cls).all()]
