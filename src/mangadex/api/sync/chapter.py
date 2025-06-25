# Contents of /mangadex-api/mangadex-api/src/mangadex/api/sync/chapter.py

import requests
from mangadex.models.chapter import Chapter
from mangadex.utils.exceptions import APIError

class ChapterAPI:
    BASE_URL = 'https://api.mangadex.org'

    @staticmethod
    def get_chapter(chapter_id):
        response = requests.get(f"{ChapterAPI.BASE_URL}/chapter/{chapter_id}")
        if response.status_code != 200:
            raise APIError(f"Error fetching chapter: {response.json()}")
        return Chapter(**response.json()['data'])

    @staticmethod
    def get_chapter_list(manga_id, limit=10, offset=0):
        response = requests.get(f"{ChapterAPI.BASE_URL}/manga/{manga_id}/aggregate", params={'limit': limit, 'offset': offset})
        if response.status_code != 200:
            raise APIError(f"Error fetching chapter list: {response.json()}")
        return [Chapter(**chapter) for chapter in response.json()['data']]

    @staticmethod
    def create_chapter(manga_id, chapter_data):
        response = requests.post(f"{ChapterAPI.BASE_URL}/chapter", json=chapter_data)
        if response.status_code != 200:
            raise APIError(f"Error creating chapter: {response.json()}")
        return Chapter(**response.json()['data'])

    @staticmethod
    def update_chapter(chapter_id, chapter_data):
        response = requests.put(f"{ChapterAPI.BASE_URL}/chapter/{chapter_id}", json=chapter_data)
        if response.status_code != 200:
            raise APIError(f"Error updating chapter: {response.json()}")
        return Chapter(**response.json()['data'])

    @staticmethod
    def delete_chapter(chapter_id):
        response = requests.delete(f"{ChapterAPI.BASE_URL}/chapter/{chapter_id}")
        if response.status_code != 200:
            raise APIError(f"Error deleting chapter: {response.json()}")
        return response.json()