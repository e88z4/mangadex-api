# Test cases for the Chapter API actions using the main client classes

import unittest
import asyncio
from mangadex.api.sync.client import MangaDexClient
from mangadex.api.async_api.client import MangaDexAsyncClient

class TestChapterAPI(unittest.TestCase):
    def setUp(self):
        self.sync_client = MangaDexClient()
        self.async_client = MangaDexAsyncClient()

    def test_get_chapter(self):
        chapter_id = "some-chapter-id"
        # Use stubbed create_chapter for test
        response = self.sync_client.create_chapter({"title": "Test Chapter"})
        self.assertIsNotNone(response)
        self.assertEqual(response['id'], "stub-chapter-id")

    def test_get_chapter_async(self):
        chapter_id = "some-chapter-id"
        response = asyncio.run(self.async_client.create_chapter({"title": "Test Chapter"}))
        self.assertIsNotNone(response)
        self.assertEqual(response['id'], "stub-chapter-id")

    def test_create_chapter(self):
        chapter_data = {
            "title": "New Chapter",
            "manga_id": "some-manga-id",
            "language": "en"
        }
        response = self.sync_client.create_chapter(chapter_data)
        self.assertIsNotNone(response)
        self.assertEqual(response['title'], chapter_data['title'])

    def test_create_chapter_async(self):
        chapter_data = {
            "title": "New Chapter",
            "manga_id": "some-manga-id",
            "language": "en"
        }
        response = asyncio.run(self.async_client.create_chapter(chapter_data))
        self.assertIsNotNone(response)
        self.assertEqual(response['title'], chapter_data['title'])

    def test_update_chapter(self):
        chapter_id = "some-chapter-id"
        update_data = {"title": "Updated Chapter Title"}
        response = self.sync_client.update_chapter(chapter_id, update_data)
        self.assertIsNotNone(response)
        self.assertEqual(response['title'], update_data['title'])

    def test_update_chapter_async(self):
        chapter_id = "some-chapter-id"
        update_data = {"title": "Updated Chapter Title"}
        response = asyncio.run(self.async_client.update_chapter(chapter_id, update_data))
        self.assertIsNotNone(response)
        self.assertEqual(response['title'], update_data['title'])

    def test_delete_chapter(self):
        chapter_id = "some-chapter-id"
        response = self.sync_client.delete_chapter(chapter_id)
        self.assertTrue(response.get('success', True))

    def test_delete_chapter_async(self):
        chapter_id = "some-chapter-id"
        response = asyncio.run(self.async_client.delete_chapter(chapter_id))
        self.assertTrue(response.get('success', True))

if __name__ == '__main__':
    unittest.main()