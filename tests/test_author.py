# Test cases for the Author endpoints (stub/mock)

def test_get_author_list():
    """Test getting the author list (stub/mock)"""
    class DummyClient:
        def get_author_list(self, **kwargs):
            return {"result": "ok", "data": [
                {"id": "author-id-1", "name": "Author One"},
                {"id": "author-id-2", "name": "Author Two"}
            ]}
    client = DummyClient()
    response = client.get_author_list()
    assert response["result"] == "ok"
    assert isinstance(response["data"], list)
    assert all("id" in a and "name" in a for a in response["data"])

def test_create_author():
    """Test creating an author (stub/mock)"""
    class DummyClient:
        def create_author(self, data):
            return {"result": "ok", "id": "author-id-1"}
    client = DummyClient()
    response = client.create_author({"name": "Author One"})
    assert response["result"] == "ok"
    assert isinstance(response["id"], str)

def test_edit_author():
    """Test editing an author (stub/mock)"""
    class DummyClient:
        def edit_author(self, author_id, data):
            return {"result": "ok", "id": author_id}
    client = DummyClient()
    response = client.edit_author("author-id-1", {"name": "Author Updated"})
    assert response["result"] == "ok"
    assert response["id"] == "author-id-1"

def test_delete_author():
    """Test deleting an author (stub/mock)"""
    class DummyClient:
        def delete_author(self, author_id):
            return {"result": "ok"}
    client = DummyClient()
    response = client.delete_author("author-id-1")
    assert response["result"] == "ok"
