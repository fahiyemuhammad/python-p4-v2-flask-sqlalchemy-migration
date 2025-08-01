"""rename department into departments

Revision ID: 01f7c05c91ff
Revises: 534f8891f7fe
Create Date: 2025-06-11 17:22:01.427678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01f7c05c91ff'
down_revision = '534f8891f7fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
