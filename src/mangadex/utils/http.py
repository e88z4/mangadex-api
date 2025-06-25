# File: /mangadex-api/mangadex-api/src/mangadex/utils/http.py

import requests
import aiohttp
import asyncio

class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, json=None):
        response = requests.post(f"{self.base_url}{endpoint}", json=json)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, json=None):
        response = requests.put(f"{self.base_url}{endpoint}", json=json)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint):
        response = requests.delete(f"{self.base_url}{endpoint}")
        response.raise_for_status()
        return response.json()


class AsyncHttpClient:
    def __init__(self, base_url):
        self.base_url = base_url

    async def get(self, endpoint, params=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}{endpoint}", params=params) as response:
                response.raise_for_status()
                return await response.json()

    async def post(self, endpoint, json=None):
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}{endpoint}", json=json) as response:
                response.raise_for_status()
                return await response.json()

    async def put(self, endpoint, json=None):
        async with aiohttp.ClientSession() as session:
            async with session.put(f"{self.base_url}{endpoint}", json=json) as response:
                response.raise_for_status()
                return await response.json()

    async def delete(self, endpoint):
        async with aiohttp.ClientSession() as session:
            async with session.delete(f"{self.base_url}{endpoint}") as response:
                response.raise_for_status()
                return await response.json()