from typing import TYPE_CHECKING

from dao import DAOFactory
from dto import PlaylistDTO

if TYPE_CHECKING:
    from services import ServicesFactory


class PlaylistTrackService:
    def __init__(self, daos: DAOFactory, services: "ServicesFactory") -> None:
        self.daos = daos
        self.services = services

    async def add_multiple(
        self, playlist: PlaylistDTO, track_ids: list[int], publish_after_creation: bool
    ) -> PlaylistDTO:
        tracks_dto = await self.services.track_service.get_by_ids(track_ids)
        for track in tracks_dto:
            await self.daos.playlist_dao.create(playlist.id, track.id)
            await self.daos.track_dao.update(
                track.id, is_published=publish_after_creation
            )
        await self.daos.session.commit()
        return self.services.playlist_service.convert(playlist, tracks_dto)

    async def add(self, playlist_id: int, track_id: int):
        await self.daos.playlist_track_dao.create(
            playlist_id=playlist_id, track_id=track_id
        )
        await self.daos.session.commit()

    async def remove(self, playlist_id: int, track_id: int):
        await self.daos.playlist_track_dao.delete(
            playlist_id=playlist_id, track_id=track_id
        )
        await self.daos.session.commit()
