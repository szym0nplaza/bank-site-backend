"""add users table

Revision ID: d73082acfdbf
Revises: 
Create Date: 2022-11-17 17:13:02.111841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd73082acfdbf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, nullable=True),
        sa.Column('login', sa.String(50), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
        sa.Column('password', sa.String(100), nullable=False),
    )

    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_table('users')
