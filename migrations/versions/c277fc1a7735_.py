"""empty message

Revision ID: c277fc1a7735
Revises: 6984896194ae
Create Date: 2023-08-08 10:35:01.829166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c277fc1a7735'
down_revision = '6984896194ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('app_currency_code',
                            sa.String(length=5), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('app_currency_code')

    # ### end Alembic commands ###