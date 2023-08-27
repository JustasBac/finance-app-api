"""empty message

Revision ID: 131c81dc9937
Revises: 164746710e1c
Create Date: 2023-08-12 12:09:45.903226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '131c81dc9937'
down_revision = '164746710e1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('finance_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total_balance', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('finance_data', schema=None) as batch_op:
        batch_op.drop_column('total_balance')

    # ### end Alembic commands ###