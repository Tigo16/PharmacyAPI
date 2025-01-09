"""Add is_prescription_required and manufacturer index

Revision ID: 90fae251e9d8
Revises: 0a6e7adb3593
Create Date: 2025-01-09 13:14:26.551471

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90fae251e9d8'
down_revision: Union[str, None] = '0a6e7adb3593'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'drugs',
        sa.Column('is_prescription_required', sa.Boolean(), nullable=False, server_default='false')
    )

    op.create_index('ix_drugs_manufacturer', 'drugs', ['manufacturer'])


def downgrade() -> None:
    op.drop_index('ix_drugs_manufacturer', table_name='drugs')
    op.drop_column('drugs', 'is_prescription_required')