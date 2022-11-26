"""update for crypto

Revision ID: 8f1605c138e6
Revises: b3a183b2163a
Create Date: 2022-11-26 18:23:12.677076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f1605c138e6'
down_revision = 'b3a183b2163a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'crypto_daily',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('ticker', sa.String, nullable=False),
        sa.Column('date', sa.String, nullable=False),
        sa.Column('price', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('crypto_daily')
