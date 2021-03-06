"""empty message

Revision ID: 21367b936165
Revises: 3d134f1aa416
Create Date: 2017-05-02 14:54:00.500826

"""

# revision identifiers, used by Alembic.
revision = '21367b936165'
down_revision = '3d134f1aa416'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('birthdate', sa.Date(), nullable=True))
    op.add_column('users', sa.Column('picture', sa.LargeBinary(), nullable=True))
    op.add_column('users', sa.Column('title', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'title')
    op.drop_column('users', 'picture')
    op.drop_column('users', 'birthdate')
    ### end Alembic commands ###
