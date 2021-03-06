"""empty message

Revision ID: ec29e100e925
Revises: 4fabfad5a0c2
Create Date: 2018-07-08 04:11:03.263078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec29e100e925'
down_revision = '4fabfad5a0c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('challenge_points')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('challenge_points',
    sa.Column('pointid', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('pointid', name='challenge_points_pkey')
    )
    # ### end Alembic commands ###
