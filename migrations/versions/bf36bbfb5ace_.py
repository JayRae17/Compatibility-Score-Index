"""empty message

Revision ID: bf36bbfb5ace
Revises: 6418a03d2e1e
Create Date: 2020-04-27 13:23:43.682147

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bf36bbfb5ace'
down_revision = '6418a03d2e1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sets',
    sa.Column('set_id', sa.Integer(), nullable=False),
    sa.Column('set_name', sa.String(length=20), nullable=True),
    sa.Column('purpose', sa.String(length=30), nullable=True),
    sa.Column('code', sa.String(length=10), nullable=True),
    sa.Column('administrator', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['administrator'], ['organizer.user_id'], ),
    sa.PrimaryKeyConstraint('set_id'),
    sa.UniqueConstraint('set_name')
    )
    op.create_table('formedgrps',
    sa.Column('grp_id', sa.Integer(), nullable=False),
    sa.Column('set_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('criteria', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['set_id'], ['sets.set_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['regular.user_id'], ),
    sa.PrimaryKeyConstraint('grp_id')
    )
    op.create_table('joinset',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('set_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['set_id'], ['sets.set_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['regular.user_id'], ),
    sa.PrimaryKeyConstraint('user_id', 'set_id')
    )
    op.drop_table('formedgrps3')
    op.drop_table('formedgrps4')
    op.drop_table('formedgrps5')
    op.drop_table('formedgrps2')
    op.drop_table('joingroup')
    op.drop_index('group_name', table_name='grouped')
    op.drop_table('grouped')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grouped',
    sa.Column('group_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('group_name', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('purpose', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('code', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('administrator', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['administrator'], ['organizer.user_id'], name='grouped_ibfk_1'),
    sa.PrimaryKeyConstraint('group_id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('group_name', 'grouped', ['group_name'], unique=True)
    op.create_table('joingroup',
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('group_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['grouped.group_id'], name='joingroup_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['regular.user_id'], name='joingroup_ibfk_2'),
    sa.PrimaryKeyConstraint('user_id', 'group_id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('formedgrps2',
    sa.Column('minigrp_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('group_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('mbr1', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('mbr2', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('criteria', mysql.VARCHAR(length=30), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['grouped.group_id'], name='formedgrps2_ibfk_1'),
    sa.PrimaryKeyConstraint('minigrp_id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('formedgrps5',
    sa.Column('minigrp_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('group_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('mbr1', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('mbr2', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('mbr3', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('mbr4', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('mbr5', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('criteria', mysql.VARCHAR(length=30), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['grouped.group_id'], name='formedgrps5_ibfk_1'),
    sa.PrimaryKeyConstraint('minigrp_id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('formedgrps4',
    sa.Column('minigrp_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('group_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('mbr1', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('mbr2', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('mbr3', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('mbr4', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('criteria', mysql.VARCHAR(length=30), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['grouped.group_id'], name='formedgrps4_ibfk_1'),
    sa.PrimaryKeyConstraint('minigrp_id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('formedgrps3',
    sa.Column('minigrp_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('group_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('mbr1', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('mbr2', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('mbr3', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('criteria', mysql.VARCHAR(length=30), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['grouped.group_id'], name='formedgrps3_ibfk_1'),
    sa.PrimaryKeyConstraint('minigrp_id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('joinset')
    op.drop_table('formedgrps')
    op.drop_table('sets')
    # ### end Alembic commands ###
