# File: /mangadex-api/mangadex-api/src/mangadex/api/sync/group.py

import requests
from mangadex.models.group import Group
from mangadex.utils.exceptions import APIError

class MangaDexGroupAPI:
    BASE_URL = "https://api.mangadex.org"

    @staticmethod
    def get_group(group_id: str) -> Group:
        """Fetch a specific scanlation group by ID."""
        response = requests.get(f"{MangaDexGroupAPI.BASE_URL}/group/{group_id}")
        if response.status_code != 200:
            raise APIError(f"Error fetching group: {response.json()}")
        return Group(**response.json()['data'])

    @staticmethod
    def create_group(data: dict) -> Group:
        """Create a new scanlation group."""
        response = requests.post(f"{MangaDexGroupAPI.BASE_URL}/group", json=data)
        if response.status_code != 200:
            raise APIError(f"Error creating group: {response.json()}")
        return Group(**response.json()['data'])

    @staticmethod
    def update_group(group_id: str, data: dict) -> Group:
        """Update an existing scanlation group."""
        response = requests.put(f"{MangaDexGroupAPI.BASE_URL}/group/{group_id}", json=data)
        if response.status_code != 200:
            raise APIError(f"Error updating group: {response.json()}")
        return Group(**response.json()['data'])

    @staticmethod
    def delete_group(group_id: str) -> dict:
        """Delete a scanlation group."""
        response = requests.delete(f"{MangaDexGroupAPI.BASE_URL}/group/{group_id}")
        if response.status_code != 200:
            raise APIError(f"Error deleting group: {response.json()}")
        return response.json()

    @staticmethod
    def follow_group(group_id: str) -> dict:
        """Follow a scanlation group."""
        response = requests.post(f"{MangaDexGroupAPI.BASE_URL}/group/{group_id}/follow")
        if response.status_code != 200:
            raise APIError(f"Error following group: {response.json()}")
        return response.json()

    @staticmethod
    def unfollow_group(group_id: str) -> dict:
        """Unfollow a scanlation group."""
        response = requests.delete(f"{MangaDexGroupAPI.BASE_URL}/group/{group_id}/follow")
        if response.status_code != 200:
            raise APIError(f"Error unfollowing group: {response.json()}")
        return response.json()