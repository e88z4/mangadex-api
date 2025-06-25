# File: /mangadex-api/mangadex-api/src/mangadex/api/async/client.py

import aiohttp
import time
from typing import Optional, Dict, Any

class MangaDexAsyncClient:
    BASE_URL = 'https://api.mangadex.org'

    def __init__(self, base_url=None):
        self.base_url = base_url or self.BASE_URL
        self.session = None
        self.access_token = None
        self.refresh_token = None
        self.token_expires_at = 0
        self.client_id = None
        self.client_secret = None

    async def _ensure_session(self):
        """Ensure an aiohttp session exists"""
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()

    async def close(self):
        """Close the aiohttp session"""
        if self.session and not self.session.closed:
            await self.session.close()

    async def authenticate_with_client_credentials(self, client_id: str, client_secret: str) -> Dict[str, Any]:
        """
        Authenticate using OAuth2 client credentials flow (for personal clients)
        
        Args:
            client_id: Your MangaDex client ID
            client_secret: Your MangaDex client secret
            
        Returns:
            The authentication response containing tokens
        """
        await self._ensure_session()
        self.client_id = client_id
        self.client_secret = client_secret
        
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'client_credentials'
        }
        
        async with self.session.post(f"{self.base_url}/auth/token", data=data) as response:
            response_data = await response.json()
            
            if response.status == 200:
                self._set_token_data(response_data)
                
            return response_data
    
    async def authenticate_with_password(self, username: str, password: str, client_id: str, client_secret: str) -> Dict[str, Any]:
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
        await self._ensure_session()
        self.client_id = client_id
        self.client_secret = client_secret
        
        data = {
            'username': username,
            'password': password,
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'password'
        }
        
        async with self.session.post(f"{self.base_url}/auth/token", data=data) as response:
            response_data = await response.json()
            
            if response.status == 200:
                self._set_token_data(response_data)
                
            return response_data
    
    async def refresh_authentication(self) -> Dict[str, Any]:
        """
        Refresh the access token using the refresh token
        
        Returns:
            The authentication response containing new tokens
        """
        await self._ensure_session()
        
        if not self.refresh_token:
            raise ValueError("No refresh token available. Please authenticate first.")
            
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token
        }
        
        async with self.session.post(f"{self.base_url}/auth/token", data=data) as response:
            response_data = await response.json()
            
            if response.status == 200:
                self._set_token_data(response_data)
                
            return response_data
    
    def _set_token_data(self, token_data: Dict[str, Any]) -> None:
        """
        Store token data from authentication response
        
        Args:
            token_data: Authentication response data
        """
        self.access_token = token_data.get('access_token')
        self.refresh_token = token_data.get('refresh_token')
        expires_in = token_data.get('expires_in', 0)
        self.token_expires_at = time.time() + expires_in
        
    def is_authenticated(self) -> bool:
        """Check if the client has a valid authentication token"""
        return self.access_token is not None and time.time() < self.token_expires_at
    
    async def ensure_authenticated(self) -> None:
        """Ensure the client has a valid token, refreshing if necessary"""
        if not self.is_authenticated() and self.refresh_token:
            await self.refresh_authentication()
            
    def _get_auth_headers(self) -> Dict[str, str]:
        """Get headers with authentication token if available"""
        headers = {}
        if self.access_token:
            headers['Authorization'] = f'Bearer {self.access_token}'
        return headers

    async def ping(self):
        """Simple ping endpoint that doesn't require authentication"""
        await self._ensure_session()
        async with self.session.get(f"{self.base_url}/ping") as response:
            return await response.text()
            
    async def login(self, username, password):
        """Legacy login method (deprecated by MangaDex)"""
        await self._ensure_session()
        payload = {'username': username, 'password': password}
        async with self.session.post(f"{self.base_url}/auth/login", json=payload) as response:
            return await response.json()
            
    async def logout(self):
        """Legacy logout method (deprecated by MangaDex)"""
        await self._ensure_session()
        await self.ensure_authenticated()
        headers = self._get_auth_headers()
        async with self.session.post(f"{self.base_url}/auth/logout", headers=headers) as response:
            return await response.json()

    async def get_manga(self, manga_id):
        await self._ensure_session()
        await self.ensure_authenticated()
        headers = self._get_auth_headers()
        async with self.session.get(f"{self.base_url}/manga/{manga_id}", headers=headers) as response:
            return await response.json()

    async def search_manga(self, title=None, limit=10, offset=0):
        await self._ensure_session()
        await self.ensure_authenticated()
        headers = self._get_auth_headers()
        params = {'title': title, 'limit': limit, 'offset': offset}
        async with self.session.get(f"{self.base_url}/manga", params=params, headers=headers) as response:
            return await response.json()

    async def create_manga(self, manga_data):
        await self._ensure_session()
        await self.ensure_authenticated()
        headers = self._get_auth_headers()
        async with self.session.post(f"{self.base_url}/manga", json=manga_data, headers=headers) as response:
            return await response.json()

    async def update_manga(self, manga_id, manga_data):
        await self._ensure_session()
        await self.ensure_authenticated()
        headers = self._get_auth_headers()
        async with self.session.put(f"{self.base_url}/manga/{manga_id}", json=manga_data, headers=headers) as response:
            return await response.json()

    async def delete_manga(self, manga_id):
        await self._ensure_session()
        await self.ensure_authenticated()
        headers = self._get_auth_headers()
        async with self.session.delete(f"{self.base_url}/manga/{manga_id}", headers=headers) as response:
            return await response.json()

    async def get_user(self, user_id):
        await self._ensure_session()
        await self.ensure_authenticated()
        headers = self._get_auth_headers()
        async with self.session.get(f"{self.base_url}/user/{user_id}", headers=headers) as response:
            return await response.json()

    async def follow_group(self, group_id):
        await self._ensure_session()
        await self.ensure_authenticated()
        headers = self._get_auth_headers()
        async with self.session.post(f"{self.base_url}/group/{group_id}/follow", headers=headers) as response:
            return await response.json()

    async def unfollow_group(self, group_id):
        await self._ensure_session()
        await self.ensure_authenticated()
        headers = self._get_auth_headers()
        async with self.session.delete(f"{self.base_url}/group/{group_id}/follow", headers=headers) as response:
            return await response.json()

    async def get_chapter(self, chapter_id):
        await self._ensure_session()
        await self.ensure_authenticated()
        headers = self._get_auth_headers()
        async with self.session.get(f"{self.base_url}/chapter/{chapter_id}", headers=headers) as response:
            return await response.json()

    async def create_custom_list(self, list_data):
        await self._ensure_session()
        await self.ensure_authenticated()
        headers = self._get_auth_headers()
        async with self.session.post(f"{self.base_url}/list", json=list_data, headers=headers) as response:
            return await response.json()

    async def update_custom_list(self, list_id, list_data):
        await self._ensure_session()
        await self.ensure_authenticated()
        headers = self._get_auth_headers()
        async with self.session.put(f"{self.base_url}/list/{list_id}", json=list_data, headers=headers) as response:
            return await response.json()

    async def delete_custom_list(self, list_id):
        await self._ensure_session()
        await self.ensure_authenticated()
        headers = self._get_auth_headers()
        async with self.session.delete(f"{self.base_url}/list/{list_id}", headers=headers) as response:
            return await response.json()

    # Additional methods for other API actions can be added here.