"""empty message

Revision ID: 38e592483230
Revises: 0b0f8ec13862
Create Date: 2016-07-20 13:39:41.214713

"""

# revision identifiers, used by Alembic.
revision = '38e592483230'
down_revision = '0b0f8ec13862'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('dateRangeFrom', sa.Integer(), nullable=True))
    op.add_column('messages', sa.Column('dateRangeUntil', sa.Integer(), nullable=True))
    op.add_column('messages', sa.Column('timeRangeFrom', sa.Integer(), nullable=True))
    op.add_column('messages', sa.Column('timeRangeUntil', sa.Integer(), nullable=True))
    op.add_column('messages', sa.Column('weekdaysFri', sa.Boolean(), nullable=True))
    op.add_column('messages', sa.Column('weekdaysMon', sa.Boolean(), nullable=True))
    op.add_column('messages', sa.Column('weekdaysSat', sa.Boolean(), nullable=True))
    op.add_column('messages', sa.Column('weekdaysSun', sa.Boolean(), nullable=True))
    op.add_column('messages', sa.Column('weekdaysThurs', sa.Boolean(), nullable=True))
    op.add_column('messages', sa.Column('weekdaysTues', sa.Boolean(), nullable=True))
    op.add_column('messages', sa.Column('weekdaysWed', sa.Boolean(), nullable=True))
    op.drop_column('messages', 'tRangeFrom')
    op.drop_column('messages', 'tRangeUntil')
    op.drop_column('messages', 'dRangeUntil')
    op.drop_column('messages', 'sticker')
    op.drop_column('messages', 'dRangeFrom')
    op.drop_column('messages', 'weekdays')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('weekdays', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('messages', sa.Column('dRangeFrom', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('messages', sa.Column('sticker', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('messages', sa.Column('dRangeUntil', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('messages', sa.Column('tRangeUntil', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('messages', sa.Column('tRangeFrom', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('messages', 'weekdaysWed')
    op.drop_column('messages', 'weekdaysTues')
    op.drop_column('messages', 'weekdaysThurs')
    op.drop_column('messages', 'weekdaysSun')
    op.drop_column('messages', 'weekdaysSat')
    op.drop_column('messages', 'weekdaysMon')
    op.drop_column('messages', 'weekdaysFri')
    op.drop_column('messages', 'timeRangeUntil')
    op.drop_column('messages', 'timeRangeFrom')
    op.drop_column('messages', 'dateRangeUntil')
    op.drop_column('messages', 'dateRangeFrom')
    ### end Alembic commands ###
