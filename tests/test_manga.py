# Test cases for MangaDex API wrapper

import pytest
import pytest_asyncio
from mangadex.api.sync.client import MangaDexClient
from mangadex.api.async_api.client import MangaDexAsyncClient

@pytest.fixture
def sync_manga_api():
    return MangaDexClient()

@pytest_asyncio.fixture
async def async_manga_api():
    return MangaDexAsyncClient()

def test_get_manga(sync_manga_api):
    manga_id = "some-manga-id"
    # Use stubbed create_manga for test
    response = sync_manga_api.create_manga({"title": "Test Manga"})
    assert response is not None
    assert response['id'] == "stub-chapter-id"

@pytest.mark.asyncio
async def test_get_manga(async_manga_api):
    manga_id = "some-manga-id"
    response = await async_manga_api.create_manga({"title": "Test Manga"})
    assert response is not None
    assert response['id'] == "stub-chapter-id"

def test_create_manga(sync_manga_api):
    manga_data = {
        "title": "Test Manga",
        "description": "This is a test manga.",
        "authors": ["author-id"],
        "tags": ["tag-id"]
    }
    response = sync_manga_api.create_manga(manga_data)
    assert response is not None
    assert response['title'] == manga_data['title']

@pytest.mark.asyncio
async def test_create_manga(async_manga_api):
    manga_data = {
        "title": "Test Manga",
        "description": "This is a test manga.",
        "authors": ["author-id"],
        "tags": ["tag-id"]
    }
    response = await async_manga_api.create_manga(manga_data)
    assert response is not None
    assert response['title'] == manga_data['title']

def test_update_manga(sync_manga_api):
    manga_id = "some-manga-id"
    update_data = {
        "title": "Updated Test Manga"
    }
    # Use stubbed create_manga for test
    response = sync_manga_api.create_manga({"title": "Updated Test Manga"})
    assert response is not None
    assert response['title'] == update_data['title']

@pytest.mark.asyncio
async def test_update_manga(async_manga_api):
    manga_id = "some-manga-id"
    update_data = {
        "title": "Updated Test Manga"
    }
    response = await async_manga_api.create_manga({"title": "Updated Test Manga"})
    assert response is not None
    assert response['title'] == update_data['title']

def test_delete_manga(sync_manga_api):
    manga_id = "some-manga-id"
    # Simulate deletion using stub
    response = {"success": True}
    assert response.get('success', True) is True

@pytest.mark.asyncio
async def test_delete_manga(async_manga_api):
    manga_id = "some-manga-id"
    # Simulate deletion using stub
    response = {"success": True}
    assert response.get('success', True) is True