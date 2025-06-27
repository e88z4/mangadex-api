# Test cases for MangaDex API wrapper

import pytest
import pytest_asyncio
from mangadex.api import MangaDexAsyncClient

@pytest_asyncio.fixture
async def async_manga_api():
    return MangaDexAsyncClient()

@pytest.mark.asyncio
async def test_get_manga(async_manga_api):
    manga_id = "some-manga-id"
    response = await async_manga_api.get_manga(manga_id)
    assert response is not None
    assert response['id'] == manga_id
    assert 'title' in response

@pytest.mark.asyncio
async def test_search_manga(async_manga_api):
    response = await async_manga_api.search_manga(title="Test Manga")
    assert response is not None
    assert 'data' in response
    assert isinstance(response['data'], list)
    assert 'id' in response['data'][0]
    assert 'title' in response['data'][0]['attributes']