"""Add comment model

Revision ID: 40fae0de9e14
Revises: 9bbbf86486d6
Create Date: 2021-11-07 02:42:49.779837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40fae0de9e14'
down_revision = '9bbbf86486d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('pitch_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic')
    op.drop_column('users', 'bio')
    op.drop_table('comments')
    # ### end Alembic commands ###
