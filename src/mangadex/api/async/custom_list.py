# File: /mangadex-api/mangadex-api/src/mangadex/api/async/custom_list.py

import aiohttp

class MangaDexAsyncCustomList:
    def __init__(self, base_url: str, session: aiohttp.ClientSession):
        self.base_url = base_url
        self.session = session

    async def create_custom_list(self, data: dict) -> dict:
        async with self.session.post(f"{self.base_url}/list", json=data) as response:
            return await response.json()

    async def get_custom_list(self, list_id: str) -> dict:
        async with self.session.get(f"{self.base_url}/list/{list_id}") as response:
            return await response.json()

    async def update_custom_list(self, list_id: str, data: dict) -> dict:
        async with self.session.put(f"{self.base_url}/list/{list_id}", json=data) as response:
            return await response.json()

    async def delete_custom_list(self, list_id: str) -> dict:
        async with self.session.delete(f"{self.base_url}/list/{list_id}") as response:
            return await response.json()

    async def follow_custom_list(self, list_id: str) -> dict:
        async with self.session.post(f"{self.base_url}/list/{list_id}/follow") as response:
            return await response.json()

    async def unfollow_custom_list(self, list_id: str) -> dict:
        async with self.session.delete(f"{self.base_url}/list/{list_id}/follow") as response:
            return await response.json()