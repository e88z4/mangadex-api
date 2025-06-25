# File: /mangadex-api/mangadex-api/src/mangadex/api/sync/user.py

import requests
from mangadex.utils.http import HttpClient
from mangadex.models.user import UserResponse, UserListResponse
from mangadex.constants import BASE_URL

class UserAPI:
    def __init__(self, api_client: HttpClient):
        self.api_client = api_client

    def get_user(self, user_id: str) -> UserResponse:
        response = self.api_client.get(f"{BASE_URL}/user/{user_id}")
        response.raise_for_status()
        return UserResponse(**response.json())

    def delete_user(self, user_id: str) -> None:
        response = self.api_client.delete(f"{BASE_URL}/user/{user_id}")
        response.raise_for_status()

    def get_user_list(self, limit: int = 10, offset: int = 0) -> UserListResponse:
        params = {'limit': limit, 'offset': offset}
        response = self.api_client.get(f"{BASE_URL}/user", params=params)
        response.raise_for_status()
        return UserListResponse(**response.json())