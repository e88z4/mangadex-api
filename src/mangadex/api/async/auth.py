# File: /mangadex-api/mangadex-api/src/mangadex/api/async/auth.py

import aiohttp

class MangaDexAuthAsync:
    BASE_URL = 'https://api.mangadex.org'

    def __init__(self, session: aiohttp.ClientSession):
        self.session = session

    async def login(self, username: str, password: str):
        url = f"{self.BASE_URL}/auth/login"
        payload = {
            "username": username,
            "password": password
        }
        async with self.session.post(url, json=payload) as response:
            return await response.json()

    async def logout(self, token: str):
        url = f"{self.BASE_URL}/auth/logout"
        headers = {
            "Authorization": f"Bearer {token}"
        }
        async with self.session.post(url, headers=headers) as response:
            return await response.json()

    async def refresh_token(self, refresh_token: str):
        url = f"{self.BASE_URL}/auth/refresh"
        payload = {
            "refreshToken": refresh_token
        }
        async with self.session.post(url, json=payload) as response:
            return await response.json()

    async def check_permissions(self, token: str):
        url = f"{self.BASE_URL}/auth/check"
        headers = {
            "Authorization": f"Bearer {token}"
        }
        async with self.session.get(url, headers=headers) as response:
            return await response.json()