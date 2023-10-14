"""create playlist model

Revision ID: 52021a037620
Revises: 233172e87457
Create Date: 2023-09-26 09:05:56.470170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52021a037620'
down_revision = '233172e87457'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('playlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('poster_url', sa.String(length=512), nullable=True),
    sa.Column('is_private', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('poster_url', sa.String(length=512), nullable=False),
    sa.Column('is_published', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('album_tracks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.Column('track_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('tracks', sa.Column('poster_url', sa.String(length=512), nullable=True))
    op.add_column('tracks', sa.Column('track_url', sa.String(length=512), nullable=True))
    op.drop_column('tracks', 'track_path')
    op.drop_column('tracks', 'poster_path')
    op.add_column('users', sa.Column('favourite_playlist_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'playlists', ['favourite_playlist_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'favourite_playlist_id')
    op.add_column('tracks', sa.Column('poster_path', sa.VARCHAR(length=512), autoincrement=False, nullable=True))
    op.add_column('tracks', sa.Column('track_path', sa.VARCHAR(length=512), autoincrement=False, nullable=True))
    op.drop_column('tracks', 'track_url')
    op.drop_column('tracks', 'poster_url')
    op.drop_table('album_tracks')
    op.drop_table('albums')
    op.drop_table('playlists')
    # ### end Alembic commands ###
