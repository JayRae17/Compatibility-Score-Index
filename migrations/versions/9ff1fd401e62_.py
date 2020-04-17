"""empty message

Revision ID: 9ff1fd401e62
Revises: d3117bb06cc7
Create Date: 2020-04-14 16:23:50.348671

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9ff1fd401e62'
down_revision = 'd3117bb06cc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('formedgrps', sa.Column('group_id', sa.Integer(), nullable=True))
    op.add_column('formedgrps', sa.Column('minigrp_id', sa.Integer(), nullable=False))
    op.drop_constraint('formedgrps_ibfk_7', 'formedgrps', type_='foreignkey')
    op.create_foreign_key(None, 'formedgrps', 'grouped', ['group_id'], ['group_id'])
    op.drop_column('formedgrps', 'set_id')
    op.drop_column('formedgrps', 'grping_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('formedgrps', sa.Column('grping_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.add_column('formedgrps', sa.Column('set_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'formedgrps', type_='foreignkey')
    op.create_foreign_key('formedgrps_ibfk_7', 'formedgrps', 'grouped', ['set_id'], ['group_id'])
    op.drop_column('formedgrps', 'minigrp_id')
    op.drop_column('formedgrps', 'group_id')
    # ### end Alembic commands ###