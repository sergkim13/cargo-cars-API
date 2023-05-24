"""Initial migration

Revision ID: a20e0399da24
Revises: 
Create Date: 2023-05-24 13:07:30.471696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a20e0399da24'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('zip_code', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=32), nullable=False),
    sa.Column('state', sa.String(length=32), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longtitude', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('zip_code')
    )
    op.create_table('car',
    sa.Column('number_plate', sa.String(length=32), nullable=False),
    sa.Column('current_location', sa.Integer(), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.CheckConstraint("number_plate ~ '^[1-9][0-9]{3}[A-Z]$'", name='check_number_plate_pattern'),
    sa.CheckConstraint('capacity <= 1000', name='check_capacity_max'),
    sa.CheckConstraint('capacity >= 1', name='check_capacity_min'),
    sa.ForeignKeyConstraint(['current_location'], ['location.zip_code'], ),
    sa.PrimaryKeyConstraint('number_plate')
    )
    op.create_table('cargo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pickup_location', sa.Integer(), nullable=False),
    sa.Column('delivery_location', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=512), nullable=False),
    sa.CheckConstraint('weight <= 1000', name='check_weight_max'),
    sa.CheckConstraint('weight >= 1', name='check_weight_min'),
    sa.ForeignKeyConstraint(['delivery_location'], ['location.zip_code'], ),
    sa.ForeignKeyConstraint(['pickup_location'], ['location.zip_code'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cargo')
    op.drop_table('car')
    op.drop_table('location')
    # ### end Alembic commands ###