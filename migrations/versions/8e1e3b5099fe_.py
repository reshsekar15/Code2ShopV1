"""empty message

Revision ID: 8e1e3b5099fe
Revises: 9c42c16eb820
Create Date: 2018-07-15 09:50:18.458374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e1e3b5099fe'
down_revision = '9c42c16eb820'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('brands', sa.Column('couponCode', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('brands', 'couponCode')
    # ### end Alembic commands ###
