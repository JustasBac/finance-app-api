"""empty message

Revision ID: 95af5118acf3
Revises: ab58a82ece80
Create Date: 2023-08-11 08:52:40.044927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95af5118acf3'
down_revision = 'ab58a82ece80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('finance_data', schema=None) as batch_op:
        batch_op.drop_column('total_balance')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total_balance', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('total_balance')

    with op.batch_alter_table('finance_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total_balance', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))

    # ### end Alembic commands ###