# File: /mangadex-api/mangadex-api/src/mangadex/api/sync/manga.py

import requests
from mangadex.models.manga import MangaResponse, MangaCreate, MangaEdit
from mangadex.utils.exceptions import APIError

class MangaAPI:
    BASE_URL = 'https://api.mangadex.org/manga'

    @staticmethod
    def get_manga(manga_id: str) -> MangaResponse:
        response = requests.get(f"{MangaAPI.BASE_URL}/{manga_id}")
        if response.status_code == 200:
            return MangaResponse(**response.json())
        else:
            raise APIError(f"Error fetching manga: {response.status_code} - {response.text}")

    @staticmethod
    def create_manga(manga_data: MangaCreate) -> MangaResponse:
        response = requests.post(MangaAPI.BASE_URL, json=manga_data.dict())
        if response.status_code == 200:
            return MangaResponse(**response.json())
        else:
            raise APIError(f"Error creating manga: {response.status_code} - {response.text}")

    @staticmethod
    def update_manga(manga_id: str, manga_data: MangaEdit) -> MangaResponse:
        response = requests.put(f"{MangaAPI.BASE_URL}/{manga_id}", json=manga_data.dict())
        if response.status_code == 200:
            return MangaResponse(**response.json())
        else:
            raise APIError(f"Error updating manga: {response.status_code} - {response.text}")

    @staticmethod
    def delete_manga(manga_id: str) -> dict:
        response = requests.delete(f"{MangaAPI.BASE_URL}/{manga_id}")
        if response.status_code == 200:
            return {"message": "Manga deleted successfully"}
        else:
            raise APIError(f"Error deleting manga: {response.status_code} - {response.text}")

    @staticmethod
    def search_manga(query: str, limit: int = 10, offset: int = 0) -> list:
        params = {'title': query, 'limit': limit, 'offset': offset}
        response = requests.get(MangaAPI.BASE_URL, params=params)
        if response.status_code == 200:
            return [MangaResponse(**manga) for manga in response.json().get('data', [])]
        else:
            raise APIError(f"Error searching manga: {response.status_code} - {response.text}")