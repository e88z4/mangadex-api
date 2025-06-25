# Contents of /mangadex-api/mangadex-api/src/mangadex/api/async/user.py

import aiohttp

class MangaDexUserAPI:
    def __init__(self, base_url: str, session: aiohttp.ClientSession):
        self.base_url = base_url
        self.session = session

    async def get_user(self, user_id: str):
        async with self.session.get(f"{self.base_url}/user/{user_id}") as response:
            return await response.json()

    async def delete_user(self, user_id: str):
        async with self.session.delete(f"{self.base_url}/user/{user_id}") as response:
            return await response.json()

    async def get_user_custom_lists(self, user_id: str):
        async with self.session.get(f"{self.base_url}/user/{user_id}/list") as response:
            return await response.json()

    async def follow_custom_list(self, list_id: str):
        async with self.session.post(f"{self.base_url}/list/{list_id}/follow") as response:
            return await response.json()

    async def unfollow_custom_list(self, list_id: str):
        async with self.session.delete(f"{self.base_url}/list/{list_id}/follow") as response:
            return await response.json()

    async def get_logged_user_custom_lists(self):
        async with self.session.get(f"{self.base_url}/user/list") as response:
            return await response.json()