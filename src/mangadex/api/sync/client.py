# File: /mangadex-api/mangadex-api/src/mangadex/api/sync/client.py

import requests
import time
from typing import Optional, Dict, Any

class MangaDexClient:
    BASE_URL = 'https://api.mangadex.org'

    def __init__(self):
        self.session = requests.Session()
        self.access_token = None
        self.refresh_token = None
        self.token_expires_at = 0
        self.client_id = None
        self.client_secret = None

    def authenticate_with_client_credentials(self, client_id: str, client_secret: str) -> Dict[str, Any]:
        """
        Authenticate using OAuth2 client credentials flow (for personal clients)
        """
        self.client_id = client_id
        self.client_secret = client_secret
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'client_credentials'
        }
        response = self.session.post(f'{self.BASE_URL}/auth/token', data=data)
        response_data = response.json()
        if response.status_code == 200:
            self._set_token_data(response_data)
        return response_data

    def authenticate_with_password(self, username: str, password: str, client_id: str, client_secret: str) -> Dict[str, Any]:
        """
        Authenticate using OAuth2 password flow (for personal clients)
        
        Args:
            username: Your MangaDex username
            password: Your MangaDex password
            client_id: Your MangaDex client ID
            client_secret: Your MangaDex client secret
            
        Returns:
            The authentication response containing tokens
        """
        self.client_id = client_id
        self.client_secret = client_secret
        data = {
            'username': username,
            'password': password,
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'password'
        }
        response = self.session.post(f'{self.BASE_URL}/auth/token', data=data)
        response_data = response.json()
        if response.status_code == 200:
            self._set_token_data(response_data)
        return response_data

    def refresh_authentication(self) -> Dict[str, Any]:
        """
        Refresh the access token using the refresh token
        """
        if not self.refresh_token:
            raise ValueError("No refresh token available. Please authenticate first.")
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token
        }
        response = self.session.post(f'{self.BASE_URL}/auth/token', data=data)
        response_data = response.json()
        if response.status_code == 200:
            self._set_token_data(response_data)
        return response_data

    def _set_token_data(self, token_data: Dict[str, Any]) -> None:
        self.access_token = token_data.get('access_token')
        self.refresh_token = token_data.get('refresh_token')
        expires_in = token_data.get('expires_in', 0)
        self.token_expires_at = time.time() + expires_in

    def is_authenticated(self) -> bool:
        return self.access_token is not None and time.time() < self.token_expires_at

    def ensure_authenticated(self) -> None:
        if not self.is_authenticated() and self.refresh_token:
            self.refresh_authentication()

    def _get_auth_headers(self) -> Dict[str, str]:
        headers = {}
        if self.access_token:
            headers['Authorization'] = f'Bearer {self.access_token}'
        return headers

    def ping(self):
        response = self.session.get(f'{self.BASE_URL}/ping')
        return response.text

    def login(self, username, password):
        response = self.session.post(f'{self.BASE_URL}/auth/login', json={'username': username, 'password': password})
        return response.json()

    def get_manga(self, manga_id):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.get(f'{self.BASE_URL}/manga/{manga_id}', headers=headers)
        return response.json()

    def create_manga(self, manga_data):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.post(f'{self.BASE_URL}/manga', json=manga_data, headers=headers)
        return response.json()

    def update_manga(self, manga_id, manga_data):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.put(f'{self.BASE_URL}/manga/{manga_id}', json=manga_data, headers=headers)
        return response.json()

    def delete_manga(self, manga_id):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.delete(f'{self.BASE_URL}/manga/{manga_id}', headers=headers)
        return response.json()

    def get_user(self, user_id):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.get(f'{self.BASE_URL}/user/{user_id}', headers=headers)
        return response.json()

    def follow_group(self, group_id):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.post(f'{self.BASE_URL}/group/{group_id}/follow', headers=headers)
        return response.json()

    def unfollow_group(self, group_id):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.delete(f'{self.BASE_URL}/group/{group_id}/follow', headers=headers)
        return response.json()

    # --- Chapter endpoints ---
    def create_chapter(self, chapter_data):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.post(f'{self.BASE_URL}/chapter', json=chapter_data, headers=headers)
        return response.json()

    def update_chapter(self, chapter_id, update_data):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.put(f'{self.BASE_URL}/chapter/{chapter_id}', json=update_data, headers=headers)
        return response.json()

    def delete_chapter(self, chapter_id):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.delete(f'{self.BASE_URL}/chapter/{chapter_id}', headers=headers)
        return response.json()

    # --- Custom List endpoints ---
    def get_custom_list(self, list_id):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.get(f'{self.BASE_URL}/list/{list_id}', headers=headers)
        return response.json()

    # --- Group endpoints ---
    def get_group(self, group_id):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.get(f'{self.BASE_URL}/group/{group_id}', headers=headers)
        return response.json()

    def create_group(self, group_data):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.post(f'{self.BASE_URL}/group', json=group_data, headers=headers)
        return response.json()

    def update_group(self, group_id, update_data):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.put(f'{self.BASE_URL}/group/{group_id}', json=update_data, headers=headers)
        return response.json()

    def delete_group(self, group_id):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.delete(f'{self.BASE_URL}/group/{group_id}', headers=headers)
        return response.json()

    # --- User endpoints ---
    def delete_user(self, user_id):
        self.ensure_authenticated()
        headers = self._get_auth_headers()
        response = self.session.delete(f'{self.BASE_URL}/user/{user_id}', headers=headers)
        return response.json()
        
    # --- At Home endpoints ---
    def get_chapter_server(self, chapter_id):
        """
        Get MangaDex@Home server URL for a chapter
        
        Args:
            chapter_id: ID of the chapter
            
        Returns:
            Server information including baseUrl, chapter hash and filenames
        """
        response = self.session.get(f"{self.BASE_URL}/at-home/server/{chapter_id}")
        return response.json()
        
    def get_chapter_image_urls(self, at_home_data, use_data_saver=False):
        """
        Construct image URLs from at-home API data
        
        Args:
            at_home_data: Response from get_chapter_server
            use_data_saver: Use data saver server if True (compressed images)
            
        Returns:
            List of image URLs
        """
        base_url = at_home_data["baseUrl"]
        chapter_hash = at_home_data["chapter"]["hash"]
        
        # Choose quality
        key = "dataSaver" if use_data_saver else "data"
        filenames = at_home_data["chapter"][key]
        
        # Construct URLs
        server = "data-saver" if use_data_saver else "data"
        return [f"{base_url}/{server}/{chapter_hash}/{filename}" for filename in filenames]