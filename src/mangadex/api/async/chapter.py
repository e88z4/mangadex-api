# Contents of /mangadex-api/mangadex-api/src/mangadex/api/async/chapter.py

import aiohttp

class MangaDexChapterAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def get_chapter(self, chapter_id: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/chapter/{chapter_id}") as response:
                return await response.json()

    async def create_chapter(self, chapter_data: dict):
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/chapter", json=chapter_data) as response:
                return await response.json()

    async def update_chapter(self, chapter_id: str, chapter_data: dict):
        async with aiohttp.ClientSession() as session:
            async with session.put(f"{self.base_url}/chapter/{chapter_id}", json=chapter_data) as response:
                return await response.json()

    async def delete_chapter(self, chapter_id: str):
        async with aiohttp.ClientSession() as session:
            async with session.delete(f"{self.base_url}/chapter/{chapter_id}") as response:
                return await response.json()