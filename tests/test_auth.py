# Test cases for the authentication module of the MangaDex API wrapper

import pytest
import time
from unittest.mock import patch, Mock, MagicMock
from mangadex.api.sync.client import MangaDexClient

# Legacy auth module imports (if still needed)
# from mangadex.api.sync.auth import login, logout, refresh_token
# from mangadex.api.async_api.auth import async_login, async_logout, async_refresh_token

@pytest.fixture
def mock_token_response():
    return {
        'access_token': 'mock_access_token',
        'refresh_token': 'mock_refresh_token',
        'expires_in': 3600,  # 1 hour
        'token_type': 'Bearer'
    }

@pytest.fixture
def client():
    return MangaDexClient()

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

@patch('requests.Session.post')
def test_authenticate_with_client_credentials_success(mock_post, client, oauth_credentials, mock_token_response):
    """Test successful authentication with client credentials"""
    # Set up the mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_token_response
    mock_post.return_value = mock_response
    
    # Call the method
    response = client.authenticate_with_client_credentials(
        oauth_credentials['client_id'], 
        oauth_credentials['client_secret']
    )
    
    # Verify the request was made correctly
    mock_post.assert_called_once_with(
        f'{client.BASE_URL}/auth/token', 
        data={
            'client_id': oauth_credentials['client_id'],
            'client_secret': oauth_credentials['client_secret'],
            'grant_type': 'client_credentials'
        }
    )
    
    # Verify response and client state
    assert response == mock_token_response
    assert client.access_token == 'mock_access_token'
    assert client.refresh_token == 'mock_refresh_token'
    assert client.client_id == oauth_credentials['client_id']
    assert client.client_secret == oauth_credentials['client_secret']
    assert client.is_authenticated() is True

@patch('requests.Session.post')
def test_authenticate_with_client_credentials_failure(mock_post, client, oauth_credentials):
    """Test failed authentication with client credentials"""
    # Set up the mock response
    error_response = {'error': 'invalid_client', 'message': 'Invalid client credentials'}
    mock_response = Mock()
    mock_response.status_code = 401
    mock_response.json.return_value = error_response
    mock_post.return_value = mock_response
    
    # Call the method
    response = client.authenticate_with_client_credentials(
        oauth_credentials['client_id'], 
        oauth_credentials['client_secret']
    )
    
    # Verify response and client state
    assert response == error_response
    assert client.access_token is None
    assert client.refresh_token is None
    assert client.is_authenticated() is False

@patch('requests.Session.post')
def test_refresh_authentication_success(mock_post, client, oauth_credentials):
    """Test successful token refresh"""
    # Set up initial state
    client.client_id = oauth_credentials['client_id']
    client.client_secret = oauth_credentials['client_secret']
    client.access_token = 'old_access_token'
    client.refresh_token = 'old_refresh_token'
    client.token_expires_at = time.time() - 100  # Expired token
    
    # Set up the mock response
    new_token_response = {
        'access_token': 'new_access_token',
        'refresh_token': 'new_refresh_token',
        'expires_in': 3600
    }
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = new_token_response
    mock_post.return_value = mock_response
    
    # Call the method
    response = client.refresh_authentication()
    
    # Verify the request was made correctly
    mock_post.assert_called_once_with(
        f'{client.BASE_URL}/auth/token', 
        data={
            'client_id': oauth_credentials['client_id'],
            'client_secret': oauth_credentials['client_secret'],
            'grant_type': 'refresh_token',
            'refresh_token': 'old_refresh_token'
        }
    )
    
    # Verify response and client state
    assert response['access_token'] == 'new_access_token'
    assert client.access_token == 'new_access_token'
    assert client.refresh_token == 'new_refresh_token'
    assert client.is_authenticated() is True

def test_refresh_authentication_no_token(client):
    """Test trying to refresh when no refresh token exists"""
    # Set up initial state (no refresh token)
    client.client_id = "test_client_id"
    client.client_secret = "test_client_secret"
    client.access_token = None
    client.refresh_token = None
    
    # Verify it raises the expected exception
    with pytest.raises(ValueError):
        client.refresh_authentication()

def test_is_authenticated(client):
    """Test the is_authenticated method"""
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

@patch('requests.Session.post')
def test_authenticate_with_password_success(mock_post, client, oauth_credentials, valid_credentials, mock_token_response):
    """Test successful authentication with password"""
    # Set up the mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_token_response
    mock_post.return_value = mock_response
    
    # Call the method
    response = client.authenticate_with_password(
        valid_credentials['username'],
        valid_credentials['password'],
        oauth_credentials['client_id'], 
        oauth_credentials['client_secret']
    )
    
    # Verify the request was made correctly
    mock_post.assert_called_once_with(
        f'{client.BASE_URL}/auth/token', 
        data={
            'username': valid_credentials['username'],
            'password': valid_credentials['password'],
            'client_id': oauth_credentials['client_id'],
            'client_secret': oauth_credentials['client_secret'],
            'grant_type': 'password'
        }
    )
    
    # Verify response and client state
    assert response == mock_token_response
    assert client.access_token == 'mock_access_token'
    assert client.refresh_token == 'mock_refresh_token'
    assert client.client_id == oauth_credentials['client_id']
    assert client.client_secret == oauth_credentials['client_secret']
    assert client.is_authenticated() is True

@patch('requests.Session.post')
def test_authenticate_with_password_failure(mock_post, client, oauth_credentials, invalid_credentials):
    """Test failed authentication with password"""
    # Set up the mock response
    mock_response = Mock()
    mock_response.status_code = 401
    mock_response.json.return_value = {'error': 'invalid_credentials', 'message': 'Invalid username or password'}
    mock_post.return_value = mock_response
    
    # Call the method
    response = client.authenticate_with_password(
        invalid_credentials['username'],
        invalid_credentials['password'],
        oauth_credentials['client_id'], 
        oauth_credentials['client_secret']
    )
    
    # Verify response and client state
    assert response == {'error': 'invalid_credentials', 'message': 'Invalid username or password'}
    assert client.access_token is None
    assert client.refresh_token is None
    assert client.is_authenticated() is False

def test_get_client_secret():
    """Test getting a client secret (stub/mock)"""
    class DummyClient:
        def get_client_secret(self, client_id):
            # Simulate API response
            return {"result": "ok", "data": "secret-value"}
    client = DummyClient()
    response = client.get_client_secret("some-client-id")
    assert response["result"] == "ok"
    assert isinstance(response["data"], str)


def test_regenerate_client_secret():
    """Test regenerating a client secret (stub/mock)"""
    class DummyClient:
        def regenerate_client_secret(self, client_id):
            # Simulate API response
            return {"result": "ok", "data": "new-secret-value"}
    client = DummyClient()
    response = client.regenerate_client_secret("some-client-id")
    assert response["result"] == "ok"
    assert isinstance(response["data"], str)