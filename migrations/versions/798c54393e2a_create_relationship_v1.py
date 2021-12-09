"""create relationship v1

Revision ID: 798c54393e2a
Revises: f1b3691be8f6
Create Date: 2021-12-09 17:08:14.469403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '798c54393e2a'
down_revision = 'f1b3691be8f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clients', sa.Column('professional_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'clients', 'professional', ['professional_id'], ['id'])
    op.create_foreign_key(None, 'professional_rating', 'professional', ['professional_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'professional_rating', type_='foreignkey')
    op.drop_constraint(None, 'clients', type_='foreignkey')
    op.drop_column('clients', 'professional_id')
    # ### end Alembic commands ###