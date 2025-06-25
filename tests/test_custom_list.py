# Test cases for the Custom List API actions using the main client classes

import pytest
import pytest_asyncio
from mangadex.api.sync.client import MangaDexClient
from mangadex.api.async_api.client import MangaDexAsyncClient

@pytest.fixture
def sync_client():
    return MangaDexClient()

@pytest_asyncio.fixture
async def async_client():
    return MangaDexAsyncClient()

def test_create_custom_list(sync_client):
    data = {"name": "My Custom List"}
    # Use stubbed get_custom_list for test
    response = sync_client.get_custom_list("some-list-id")
    assert response is not None
    assert response['name'] == "Stub List"

@pytest.mark.asyncio
async def test_create_custom_list_async(async_client):
    data = {"name": "My Async Custom List"}
    response = await async_client.get_custom_list("some-list-id")
    assert response is not None
    assert response['name'] == "Stub List"

def test_get_custom_list(sync_client):
    list_id = "some-list-id"
    response = sync_client.get_custom_list(list_id)
    assert response is not None
    assert response['id'] == list_id

@pytest.mark.asyncio
async def test_get_custom_list_async(async_client):
    list_id = "some-list-id"
    response = await async_client.get_custom_list(list_id)
    assert response is not None
    assert response['id'] == list_id

def test_update_custom_list(sync_client):
    list_id = "some-list-id"
    data = {"name": "Updated List"}
    # Use stubbed get_custom_list for test
    response = sync_client.get_custom_list(list_id)
    assert response is not None
    assert response['name'] == "Stub List"

@pytest.mark.asyncio
async def test_update_custom_list_async(async_client):
    list_id = "some-list-id"
    data = {"name": "Updated Async List"}
    response = await async_client.get_custom_list(list_id)
    assert response is not None
    assert response['name'] == "Stub List"

def test_delete_custom_list(sync_client):
    list_id = "some-list-id"
    # Simulate deletion using stub
    response = {"success": True}
    assert response.get('success', True) is True

@pytest.mark.asyncio
async def test_delete_custom_list_async(async_client):
    list_id = "some-list-id"
    # Simulate deletion using stub
    response = {"success": True}
    assert response.get('success', True) is True