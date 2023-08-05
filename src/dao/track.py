from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAO
from models import Track, User


class TrackDAO(BaseDAO[Track]):
    def __init__(self, session: AsyncSession):
        super().__init__(Track, session)

    async def create(self, user_id: int, title: str, poster_path: str) -> Track:
        track = Track(
            user_id=user_id,
            title=title,
            poster_path=poster_path,
        )
        self.session.add(track)
        await self.session.commit()
        await self.session.refresh(track)
        return track

    async def get_by_username(self, username: str) -> Track:
        stmt = select(Track).where(
            (Track.user_id == User.id) & (User.username == username)
        )
        result = await self.session.scalars(stmt)
        return result.all()
