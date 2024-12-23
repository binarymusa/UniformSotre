"""added gender and category

Revision ID: d5da671ccb23
Revises: 7c34d4ee1137
Create Date: 2024-10-31 11:58:54.603069

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd5da671ccb23'
down_revision = '7c34d4ee1137'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('outfits', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gender', sa.String(length=60), nullable=False))
        batch_op.add_column(sa.Column('category', sa.String(length=60), nullable=False))
        batch_op.drop_column('Type')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('outfits', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Type', mysql.VARCHAR(length=60), nullable=False))
        batch_op.drop_column('category')
        batch_op.drop_column('gender')

    # ### end Alembic commands ###
