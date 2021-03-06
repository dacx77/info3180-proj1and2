"""empty message

Revision ID: 2b11266a2332
Revises: None
Create Date: 2016-03-06 15:55:01.699815

"""

# revision identifiers, used by Alembic.
revision = '2b11266a2332'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('myprofile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('sex', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('myprofile')
    ### end Alembic commands ###
