"""empty message

Revision ID: 403e132911ef
Revises: db4987b2ba9d
Create Date: 2017-07-03 14:36:21.097963

"""

# revision identifiers, used by Alembic.
revision = '403e132911ef'
down_revision = 'db4987b2ba9d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('organization_memberships', sa.Column('mobile', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('organization_memberships', 'mobile')
    ### end Alembic commands ###
