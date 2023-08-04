"""empty message

Revision ID: 130c8d920eb4
Revises: f9f2c825c0ed
Create Date: 2023-08-04 10:40:07.645341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '130c8d920eb4'
down_revision = 'f9f2c825c0ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('finances')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('finances',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_by_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['users.id'], name='finances_created_by_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='finances_pkey')
    )
    # ### end Alembic commands ###