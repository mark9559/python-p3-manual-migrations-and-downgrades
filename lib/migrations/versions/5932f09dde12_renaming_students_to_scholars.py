"""Renaming students to scholars

Revision ID: 5932f09dde12
Revises: 791279dd0760
Create Date: 2023-12-06 01:00:38.235128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5932f09dde12'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')



def downgrade() -> None:
    op.rename_table('scholars', 'students')

