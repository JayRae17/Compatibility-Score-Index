"""empty message

Revision ID: 8c212dd75d7b
Revises: 
Create Date: 2020-05-07 21:35:59.400780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c212dd75d7b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userscore',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('other_id', sa.Integer(), nullable=False),
    sa.Column('score', sa.DECIMAL(precision=4, scale=3), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['regular.user_id'], ),
    sa.PrimaryKeyConstraint('user_id', 'other_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userscore')
    # ### end Alembic commands ###