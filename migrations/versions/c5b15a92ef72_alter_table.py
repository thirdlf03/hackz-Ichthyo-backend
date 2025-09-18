"""alter table

Revision ID: c5b15a92ef72
Revises: b88f2f1c0a78
Create Date: 2025-09-18 02:49:42.308610

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5b15a92ef72'
down_revision: Union[str, Sequence[str], None] = 'b88f2f1c0a78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
