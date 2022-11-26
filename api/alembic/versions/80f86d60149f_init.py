"""init

Revision ID: 80f86d60149f
Revises: 
Create Date: 2022-11-24 22:34:27.147058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80f86d60149f'
down_revision = None
branch_labels = None
depends_on = None



def upgrade():
    op.create_table(
        'entities',
        sa.Column('id', sa.Integer, primary_key=True), # 1
        sa.Column('title', sa.String, nullable=False), # BTC
        sa.Column('market', sa.String, nullable=True), # Cryptocurrency
        sa.Column('description', sa.String, nullable=True) # Bla bla bla...
    )


def downgrade():
    op.drop_table('entities')
