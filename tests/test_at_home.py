# Test cases for the /at-home/server/{chapterId} endpoint (stub/mock)

def test_get_at_home_server():
    """Test getting at-home server info for a chapter (stub/mock)"""
    class DummyClient:
        def get_at_home_server(self, chapter_id):
            return {"result": "ok", "baseUrl": "https://uploads.mangadex.org", "chapter": {"id": chapter_id}}
    client = DummyClient()
    response = client.get_at_home_server("chapter-id-1")
    assert response["result"] == "ok"
    assert response["baseUrl"].startswith("https://")
    assert response["chapter"]["id"] == "chapter-id-1"
