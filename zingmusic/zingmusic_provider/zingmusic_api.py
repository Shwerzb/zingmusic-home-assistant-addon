import aiohttp

GRAPHQL_URL = "https://jewishmusic.fm:8443/graphql"
MEDIA_BASE_URL = "https://jewishmusic.fm/wp-content/uploads/secretmusicfolder1/"

class ZingMusicAPI:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def _post(self, query: str, variables: dict):
        async with self.session.post(
            GRAPHQL_URL,
            json={"query": query, "variables": variables},
            headers={"Content-Type": "application/json"}
        ) as resp:
            result = await resp.json()
            return result.get("data", {})

    async def search_albums(self, term: str):
        query = """
        query Search($term: String!) {
            albums(where: {enName: {contains: $term}}, take: 10, orderBy: {id: desc}) {
                id
                enName
                artists { enName }
                images { large }
            }
        }
        """
        data = await self._post(query, {"term": term})
        return [
            {
                "id": a["id"],
                "title": a["enName"],
                "artist": a["artists"][0]["enName"] if a["artists"] else "Unknown",
                "image": a["images"]["large"] if a.get("images") else None
            }
            for a in data.get("albums", [])
        ]

    async def get_album(self, album_id: int):
        query = """
        query GetAlbumDetail($id: Int!) {
            album(where: {id: $id}) {
                id
                enName
                images { large }
                artists { enName }
                tracks(orderBy: {trackNumber: asc}) {
                    id
                    enName
                    file
                }
            }
        }
        """
        data = await self._post(query, {"id": album_id})
        album = data.get("album", {})
        return {
            "id": album["id"],
            "title": album["enName"],
            "artist": album["artists"][0]["enName"] if album.get("artists") else "Unknown",
            "image": album["images"]["large"] if album.get("images") else None,
            "tracks": [
                {
                    "id": t["id"],
                    "title": t["enName"],
                    "url": MEDIA_BASE_URL + t["file"]
                }
                for t in album.get("tracks", []) if t.get("file")
            ]
        }

    async def get_track_url(self, track_id: int) -> str:
        # This could be improved to support standalone track lookups if needed.
        raise NotImplementedError("ZingMusic only resolves track URLs via album context.")

    async def list_recent_albums(self):
        # For browsing or 'library' view
        return await self.search_albums("")  # Fetch latest by leaving search blank

    async def close(self):
        await self.session.close()
