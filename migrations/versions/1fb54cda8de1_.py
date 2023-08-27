"""empty message

Revision ID: 1fb54cda8de1
Revises: eb6ebbd0adee
Create Date: 2023-08-13 09:36:24.443068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fb54cda8de1'
down_revision = 'eb6ebbd0adee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('finance_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('datetime', sa.DateTime(), nullable=False))
        batch_op.drop_column('month')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('finance_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('month', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.drop_column('datetime')

    # ### end Alembic commands ###