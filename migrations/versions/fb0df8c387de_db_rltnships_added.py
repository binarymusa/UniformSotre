"""db rltnships added

Revision ID: fb0df8c387de
Revises: 4c3695cd8aa6
Create Date: 2024-11-04 10:20:44.509980

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fb0df8c387de'
down_revision = '4c3695cd8aa6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.add_column(sa.Column('outfit_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('cart_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'outfits', ['outfit_id'], ['id'])
        batch_op.drop_column('outfits_id')

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('outfit_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'outfits', ['outfit_id'], ['id'])
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')
        batch_op.drop_column('outfit_id')

    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.add_column(sa.Column('outfits_id', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('cart_ibfk_1', 'outfits', ['outfits_id'], ['id'])
        batch_op.drop_column('outfit_id')

    # ### end Alembic commands ###
