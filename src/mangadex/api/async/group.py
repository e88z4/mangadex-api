# File: /mangadex-api/mangadex-api/src/mangadex/api/async/group.py

import httpx

class MangaDexGroupAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def get_group(self, group_id: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/group/{group_id}")
            response.raise_for_status()
            return response.json()

    async def create_group(self, group_data: dict):
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/group", json=group_data)
            response.raise_for_status()
            return response.json()

    async def update_group(self, group_id: str, group_data: dict):
        async with httpx.AsyncClient() as client:
            response = await client.put(f"{self.base_url}/group/{group_id}", json=group_data)
            response.raise_for_status()
            return response.json()

    async def delete_group(self, group_id: str):
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"{self.base_url}/group/{group_id}")
            response.raise_for_status()
            return response.json()

    async def follow_group(self, group_id: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/group/{group_id}/follow")
            response.raise_for_status()
            return response.json()

    async def unfollow_group(self, group_id: str):
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"{self.base_url}/group/{group_id}/follow")
            response.raise_for_status()
            return response.json()