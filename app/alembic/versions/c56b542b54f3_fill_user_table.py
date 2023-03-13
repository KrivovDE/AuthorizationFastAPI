"""fill user table

Revision ID: c56b542b54f3
Revises: 53e620ca8c3c
Create Date: 2023-03-13 00:00:03.840627

"""
from alembic import op
import sqlalchemy as sa

from app.models.user import User
from sqlalchemy import orm, table, column

from app.scheme import UserInDB

# revision identifiers, used by Alembic.
revision = 'c56b542b54f3'
down_revision = '53e620ca8c3c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    u1 = User(
        id=1,
        props={
            "username": "avm",
            "full_name": "Alex M",
            "email": "johndoe@example.com",
            "hashed_password": "$2b$12$9NNTn/9E69sYg0Kqcvgogu5QSvzA2klekjTku6FKaCMTSvaMaWgGm",
            "is_active": "1",
            "is_admin": "1"
        }
    )
    u2 = User(
        id=2,
        props={
            "username": "test_1",
            "full_name": "test_1",
            "email": "johndoe@example.com",
            "hashed_password": "$2b$12$S49KbwUQXe4YloN68eStxeC0ybBoNakM5yakbpUv2nT2En5qoJB1W",
            "is_active": "0",
            "is_admin": "0"
        }
    )
    u3 = User(
        id=3,
        props={
            "username": "test_2",
            "full_name": "test_2",
            "email": "johndoe@example.com",
            "hashed_password": "$2b$12$wapwh71lY.Txv3Yq57lfJeT6JZssfEjmh9HuDYDzvmNJscqaCQi.O",
            "is_active": "1",
            "is_admin": "0"
        }
    )
    u4 = User(
        id=4,
        props={
            "username": "test_3",
            "full_name": "test_3",
            "email": "johndoe@example.com",
            "hashed_password": "$2b$12$4MdyLi6fwpcmdjI1s4ebVO95x.p7OmQOJ7Sb9pWaO7fw4QjB/cmoC",
            "is_active": "1",
            "is_admin": "0"
        }
    )
    u5 = User(
        id= 5,
        props= {
             "username": "test_4",
             "full_name": "test_4",
             "email": "johndoe@example.com",
             "hashed_password": "$2b$12$rMZeaqqcj5jRrEHTJ01pne8h9hbGz9GCQGl/2aZ1kqkJ0X/IpUdES",
             "is_active": "1",
             "is_admin": "0"

         }
    )


    # session.add(u1)
    session.add_all([u1, u2, u3, u4, u5])
    session.commit()


def downgrade() -> None:
    pass
