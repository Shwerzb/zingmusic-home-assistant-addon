from __future__ import annotations
from typing import List, Optional
from music_assistant.common.models.config_entry import ConfigEntry
from music_assistant.common.models.media_items import Album, Track, Artist
from music_assistant.server.controllers.streams import MultiFormatAudioProvider
from music_assistant.server.models.music_provider import MusicProvider
from .zingmusic_api import ZingMusicAPI

class ZingMusicProvider(MusicProvider, MultiFormatAudioProvider):
    """Custom Music Assistant provider for ZingMusic.app."""

    _api: ZingMusicAPI

    async def setup(self, config: ConfigEntry) -> bool:
        self._api = ZingMusicAPI()
        return True

    @property
    def name(self) -> str:
        return "ZingMusic"

    @property
    def supported_features(self) -> tuple[str, ...]:
        return ("search", "streaming", "browse", "library")

    async def search(self, search_query: str, media_types: Optional[List[str]] = None, limit: int = 10):
        results = await self._api.search_albums(search_query)
        albums = []
        for item in results[:limit]:
            artist = Artist(item["artist"], provider=self.instance_id)
            albums.append(
                Album(
                    item["title"],
                    provider=self.instance_id,
                    album_id=str(item["id"]),
                    artists=[artist],
                    year=None,
                    image=item["image"],
                )
            )
        return {"albums": albums}

    async def get_album(self, prov_album_id: str) -> Album:
        data = await self._api.get_album(int(prov_album_id))
        album = Album(
            data["title"],
            provider=self.instance_id,
            album_id=str(data["id"]),
            artists=[Artist(data["artist"], provider=self.instance_id)],
            image=data["image"],
            tracks=[],
        )
        for i, t in enumerate(data["tracks"]):
            album.tracks.append(
                Track(
                    name=t["title"],
                    provider=self.instance_id,
                    track_id=str(t["id"]),
                    album=album,
                    sort_order=i,
                    artists=[Artist(data["artist"], provider=self.instance_id)],
                    media_url=t["url"]
                )
            )
        return album

    async def get_track_stream_url(self, prov_track_id: str) -> str:
        url = await self._api.get_track_url(int(prov_track_id))
        return url

    async def get_library_albums(self) -> List[Album]:
        items = await self._api.list_recent_albums()
        return [
            Album(
                item["title"],
                provider=self.instance_id,
                album_id=str(item["id"]),
                artists=[Artist(item["artist"], provider=self.instance_id)],
                image=item["image"],
            )
            for item in items
        ]
