"""big integer

Revision ID: c3046425f772
Revises: 
Create Date: 2018-11-05 03:57:13.271484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3046425f772'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def upgrade_team_db():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team_members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('phone_number', sa.BigInteger(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('role', sa.Enum('admin', 'regular', name='teammemberenum'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('team_members', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_team_members_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_team_members_first_name'), ['first_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_team_members_last_name'), ['last_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_team_members_phone_number'), ['phone_number'], unique=True)

    # ### end Alembic commands ###


def downgrade_team_db():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('team_members', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_team_members_phone_number'))
        batch_op.drop_index(batch_op.f('ix_team_members_last_name'))
        batch_op.drop_index(batch_op.f('ix_team_members_first_name'))
        batch_op.drop_index(batch_op.f('ix_team_members_email'))

    op.drop_table('team_members')
    # ### end Alembic commands ###

