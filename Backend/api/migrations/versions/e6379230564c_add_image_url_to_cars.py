"""add image_url to cars

Revision ID: e6379230564c
Revises: 685ffe728d14
Create Date: 2025-05-30 14:49:31.200650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6379230564c'
down_revision: Union[str, None] = '685ffe728d14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        'cars',
        'preco_diaria',
        existing_type=sa.VARCHAR(),
        type_=sa.Float(),
        existing_nullable=False,
        postgresql_using='preco_diaria::double precision'
    )
    op.add_column('cars', sa.Column('image_url', sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('cars', 'image_url')
    op.alter_column(
        'cars',
        'preco_diaria',
        existing_type=sa.Float(),
        type_=sa.VARCHAR(),
        existing_nullable=False,
        postgresql_using='preco_diaria::VARCHAR'
    )
