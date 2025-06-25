# Contents of /mangadex-api/mangadex-api/src/mangadex/api/async/manga.py

import aiohttp

class MangaDexAsyncAPI:
    BASE_URL = "https://api.mangadex.org"

    def __init__(self, session: aiohttp.ClientSession):
        self.session = session

    async def get_manga_list(self, limit: int = 10, offset: int = 0, **params):
        url = f"{self.BASE_URL}/manga"
        params.update({"limit": limit, "offset": offset})
        async with self.session.get(url, params=params) as response:
            return await response.json()

    async def get_manga_by_id(self, manga_id: str):
        url = f"{self.BASE_URL}/manga/{manga_id}"
        async with self.session.get(url) as response:
            return await response.json()

    async def create_manga(self, manga_data: dict):
        url = f"{self.BASE_URL}/manga"
        async with self.session.post(url, json=manga_data) as response:
            return await response.json()

    async def update_manga(self, manga_id: str, manga_data: dict):
        url = f"{self.BASE_URL}/manga/{manga_id}"
        async with self.session.put(url, json=manga_data) as response:
            return await response.json()

    async def delete_manga(self, manga_id: str):
        url = f"{self.BASE_URL}/manga/{manga_id}"
        async with self.session.delete(url) as response:
            return await response.json()

    async def follow_manga(self, manga_id: str):
        url = f"{self.BASE_URL}/manga/{manga_id}/follow"
        async with self.session.post(url) as response:
            return await response.json()

    async def unfollow_manga(self, manga_id: str):
        url = f"{self.BASE_URL}/manga/{manga_id}/follow"
        async with self.session.delete(url) as response:
            return await response.json()