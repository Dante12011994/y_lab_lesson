"""try crud 3

Revision ID: 2dbadc5f6364
Revises: c54f06f21585
Create Date: 2024-01-22 23:11:43.861739

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2dbadc5f6364'
down_revision: Union[str, None] = 'c54f06f21585'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu', sa.Column('title', sa.String(), nullable=False))
    op.add_column('menu', sa.Column('description', sa.String(), nullable=False))
    op.drop_column('menu', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('menu', 'description')
    op.drop_column('menu', 'title')
    # ### end Alembic commands ###