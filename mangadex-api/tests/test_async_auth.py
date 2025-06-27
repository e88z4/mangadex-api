# File: /mangadex-api/mangadex-api/tests/test_async_auth.py

import pytest
import time
import aiohttp
from unittest.mock import patch, Mock, MagicMock
from mangadex.api import MangaDexAsyncClient

@pytest.fixture
def mock_token_response():
    return {
        'access_token': 'mock_access_token',
        'refresh_token': 'mock_refresh_token',
        'expires_in': 3600,  # 1 hour
        'token_type': 'Bearer'
    }

@pytest.fixture
def oauth_credentials():
    return {
        "client_id": "test_client_id",
        "client_secret": "test_client_secret"
    }

@pytest.fixture
def valid_credentials():
    return {
        "username": "testuser",
        "password": "testpassword"
    }

@pytest.fixture
def invalid_credentials():
    return {
        "username": "invaliduser",
        "password": "invalidpassword"
    }

class MockClientResponse:
    def __init__(self, status, json_data):
        self.status = status
        self._json_data = json_data
        
    async def json(self):
        return self._json_data
        
    async def __aenter__(self):
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

@pytest.mark.asyncio
async def test_authenticate_with_client_credentials_success(oauth_credentials, mock_token_response):
    client = MangaDexAsyncClient()
    with pytest.raises(NotImplementedError, match="password grant type"):
        await client.authenticate_with_client_credentials(
            oauth_credentials['client_id'],
            oauth_credentials['client_secret']
        )

@pytest.mark.asyncio
async def test_authenticate_with_client_credentials_failure(oauth_credentials):
    client = MangaDexAsyncClient()
    with pytest.raises(NotImplementedError, match="password grant type"):
        await client.authenticate_with_client_credentials(
            oauth_credentials['client_id'],
            oauth_credentials['client_secret']
        )

@pytest.mark.asyncio
async def test_refresh_authentication_success(oauth_credentials):
    def mock_post(url, data=None, headers=None):
        assert url == "https://auth.mangadex.org/realms/mangadex/protocol/openid-connect/token"
        assert data['grant_type'] == 'refresh_token'
        return MockClientResponse(200, {
            'access_token': 'new_access_token',
            'refresh_token': 'new_refresh_token',
            'expires_in': 3600
        })
    mock_session = MagicMock()
    mock_session.post = Mock(side_effect=mock_post)
    with patch('aiohttp.ClientSession', return_value=mock_session):
        client = MangaDexAsyncClient()
        client.client_id = oauth_credentials['client_id']
        client.client_secret = oauth_credentials['client_secret']
        client.access_token = 'old_access_token'
        client.refresh_token = 'old_refresh_token'
        client.token_expires_at = time.time() - 100
        response = await client.refresh_authentication()
        assert response['access_token'] == 'new_access_token'
        assert client.access_token == 'new_access_token'
        assert client.refresh_token == 'new_refresh_token'
        assert client.is_authenticated() is True

@pytest.mark.asyncio
async def test_refresh_authentication_no_token():
    """Test trying to refresh when no refresh token exists"""
    client = MangaDexAsyncClient()
    
    # Set up initial state (no refresh token)
    client.client_id = "test_client_id"
    client.client_secret = "test_client_secret"
    client.access_token = None
    client.refresh_token = None
    
    # Verify it raises the expected exception
    with pytest.raises(ValueError):
        await client.refresh_authentication()

def test_is_authenticated():
    """Test the is_authenticated method"""
    client = MangaDexAsyncClient()
    
    # Not authenticated initially
    assert client.is_authenticated() is False
    
    # Set token but expired
    client.access_token = 'test_token'
    client.token_expires_at = time.time() - 100
    assert client.is_authenticated() is False
    
    # Set token with future expiration
    client.token_expires_at = time.time() + 3600
    assert client.is_authenticated() is True
    
    # No token
    client.access_token = None
    assert client.is_authenticated() is False

@pytest.mark.asyncio
async def test_ensure_authenticated_with_refresh(oauth_credentials):
    from unittest.mock import AsyncMock
    client = MangaDexAsyncClient()
    client.client_id = oauth_credentials['client_id']
    client.client_secret = oauth_credentials['client_secret']
    client.access_token = 'old_access_token'
    client.refresh_token = 'old_refresh_token'
    client.token_expires_at = time.time() - 100
    client.refresh_authentication = AsyncMock(return_value={
        'access_token': 'new_access_token',
        'refresh_token': 'new_refresh_token',
        'expires_in': 3600
    })
    await client.ensure_authenticated()
    client.refresh_authentication.assert_awaited_once()

@pytest.mark.asyncio
async def test_get_auth_headers():
    """Test the _get_auth_headers method"""
    client = MangaDexAsyncClient()
    
    # No token
    headers = client._get_auth_headers()
    assert headers == {}
    
    # With token
    client.access_token = 'test_token'
    headers = client._get_auth_headers()
    assert headers == {'Authorization': 'Bearer test_token'}

@pytest.mark.asyncio
async def test_authenticate_with_password_success(oauth_credentials, valid_credentials, mock_token_response):
    def mock_post(url, data=None, headers=None):
        assert url == "https://auth.mangadex.org/realms/mangadex/protocol/openid-connect/token"
        assert data['grant_type'] == 'password'
        return MockClientResponse(200, mock_token_response)
    mock_session = MagicMock()
    mock_session.post = Mock(side_effect=mock_post)
    with patch('aiohttp.ClientSession', return_value=mock_session):
        client = MangaDexAsyncClient()
        response = await client.authenticate_with_password(
            valid_credentials['username'],
            valid_credentials['password'],
            oauth_credentials['client_id'],
            oauth_credentials['client_secret']
        )
        assert response == mock_token_response
        assert client.access_token == 'mock_access_token'
        assert client.refresh_token == 'mock_refresh_token'
        assert client.client_id == oauth_credentials['client_id']
        assert client.client_secret == oauth_credentials['client_secret']
        assert client.is_authenticated() is True

@pytest.mark.asyncio
async def test_authenticate_with_password_failure(oauth_credentials, invalid_credentials):
    def mock_post(url, data=None, headers=None):
        assert url == "https://auth.mangadex.org/realms/mangadex/protocol/openid-connect/token"
        assert data['grant_type'] == 'password'
        return MockClientResponse(401, {'error': 'invalid_client', 'error_description': 'Invalid client or Invalid client credentials'})
    mock_session = MagicMock()
    mock_session.post = Mock(side_effect=mock_post)
    with patch('aiohttp.ClientSession', return_value=mock_session):
        client = MangaDexAsyncClient()
        response = await client.authenticate_with_password(
            invalid_credentials['username'],
            invalid_credentials['password'],
            oauth_credentials['client_id'],
            oauth_credentials['client_secret']
        )
        assert 'error' in response or 'errors' in response
        assert client.access_token is None
        assert client.refresh_token is None
        assert client.is_authenticated() is False
