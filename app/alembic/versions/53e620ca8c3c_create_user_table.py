"""create user table

Revision ID: 53e620ca8c3c
Revises: 
Create Date: 2023-03-12 23:55:51.390761

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Sequence
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision = '53e620ca8c3c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, Sequence("user_id_seq", start=1), primary_key=True),
        sa.Column('props', JSONB(), nullable=False),
    )



def downgrade() -> None:
    op.drop_table('user')
