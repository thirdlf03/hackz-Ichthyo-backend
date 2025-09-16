"""create tables on rds

Revision ID: b88f2f1c0a78
Revises: b158030944b3
Create Date: 2025-09-17 00:28:25.533096

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b88f2f1c0a78'
down_revision: Union[str, Sequence[str], None] = 'b158030944b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
