"""add accounts table

Revision ID: 5aab272594df
Revises: d73082acfdbf
Create Date: 2022-11-18 14:04:17.804746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5aab272594df'
down_revision = 'd73082acfdbf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'accounts',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False, autoincrement=True),
        sa.Column('default_currency', sa.String(3), nullable=False),
        sa.Column('number', sa.String(12), nullable=False, unique=True),
        sa.Column('balance', sa.DECIMAL(precision=15,scale=2), nullable=False),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete="CASCADE"),
    )

    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_table('accounts')
