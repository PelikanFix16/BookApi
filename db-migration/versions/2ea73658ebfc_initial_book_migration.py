"""Initial book migration

Revision ID: 2ea73658ebfc
Revises: 5f90527417b3
Create Date: 2021-10-04 21:17:10.336824

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2ea73658ebfc'
down_revision = '5f90527417b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('authors', mysql.JSON(), nullable=False),
    sa.Column('published_date', sa.Integer(), nullable=False),
    sa.Column('categories', mysql.JSON(), nullable=False),
    sa.Column('average_rating', sa.Integer(), nullable=False),
    sa.Column('ratings_count', sa.Integer(), nullable=False),
    sa.Column('thumbnail', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###