"""empty message

Revision ID: 3e380d3fd07e
Revises: 1e9bed564876
Create Date: 2023-08-13 11:57:02.778232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e380d3fd07e'
down_revision = '1e9bed564876'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('saving_plans', schema=None) as batch_op:
        batch_op.add_column(sa.Column('start_date', sa.DateTime(), nullable=False))
        batch_op.add_column(sa.Column('end_date', sa.DateTime(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('saving_plans', schema=None) as batch_op:
        batch_op.drop_column('end_date')
        batch_op.drop_column('start_date')

    # ### end Alembic commands ###