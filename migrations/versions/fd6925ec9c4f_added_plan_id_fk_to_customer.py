"""added plan_id fk to customer

Revision ID: fd6925ec9c4f
Revises: f605b1635346
Create Date: 2019-08-05 13:50:22.911931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd6925ec9c4f'
down_revision = 'f605b1635346'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('plan_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'customer', 'plan', ['plan_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'customer', type_='foreignkey')
    op.drop_column('customer', 'plan_id')
    # ### end Alembic commands ###
