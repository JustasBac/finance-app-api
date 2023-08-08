"""empty message

Revision ID: 574eb595332a
Revises: c277fc1a7735
Create Date: 2023-08-08 10:41:34.407790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '574eb595332a'
down_revision = 'c277fc1a7735'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('finance_data', schema=None) as batch_op:
        batch_op.alter_column('income',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
        batch_op.alter_column('spendings',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
        batch_op.alter_column('total_balance',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('app_currency_code', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('app_currency_code')

    with op.batch_alter_table('finance_data', schema=None) as batch_op:
        batch_op.alter_column('total_balance',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
        batch_op.alter_column('spendings',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
        batch_op.alter_column('income',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)

    # ### end Alembic commands ###