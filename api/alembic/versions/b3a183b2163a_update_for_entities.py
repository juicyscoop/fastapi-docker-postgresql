"""update for entities

Revision ID: b3a183b2163a
Revises: 80f86d60149f
Create Date: 2022-11-26 17:19:27.608351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3a183b2163a'
down_revision = '80f86d60149f'
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
