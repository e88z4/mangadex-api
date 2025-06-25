# File: /mangadex-api/mangadex-api/src/mangadex/api/sync/custom_list.py

import requests
from mangadex.models.custom_list import CustomList
from mangadex.utils.exceptions import APIError

class CustomListAPI:
    BASE_URL = "https://api.mangadex.org"

    def create_custom_list(self, data):
        response = requests.post(f"{self.BASE_URL}/list", json=data)
        if response.status_code == 200:
            return CustomList(**response.json())
        else:
            raise APIError(f"Error creating custom list: {response.text}")

    def get_custom_list(self, list_id):
        response = requests.get(f"{self.BASE_URL}/list/{list_id}")
        if response.status_code == 200:
            return CustomList(**response.json())
        else:
            raise APIError(f"Error fetching custom list: {response.text}")

    def update_custom_list(self, list_id, data):
        response = requests.put(f"{self.BASE_URL}/list/{list_id}", json=data)
        if response.status_code == 200:
            return CustomList(**response.json())
        else:
            raise APIError(f"Error updating custom list: {response.text}")

    def delete_custom_list(self, list_id):
        response = requests.delete(f"{self.BASE_URL}/list/{list_id}")
        if response.status_code != 200:
            raise APIError(f"Error deleting custom list: {response.text}")

    def follow_custom_list(self, list_id):
        response = requests.post(f"{self.BASE_URL}/list/{list_id}/follow")
        if response.status_code != 200:
            raise APIError(f"Error following custom list: {response.text}")

    def unfollow_custom_list(self, list_id):
        response = requests.delete(f"{self.BASE_URL}/list/{list_id}/follow")
        if response.status_code != 200:
            raise APIError(f"Error unfollowing custom list: {response.text}")