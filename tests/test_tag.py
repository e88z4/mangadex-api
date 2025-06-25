# Test cases for the Tag endpoints (stub/mock)

def test_get_tag_list():
    """Test getting the tag list (stub/mock)"""
    class DummyClient:
        def get_tag_list(self):
            return {"result": "ok", "data": [
                {"id": "tag-id-1", "name": "Shounen"},
                {"id": "tag-id-2", "name": "Seinen"}
            ]}
    client = DummyClient()
    response = client.get_tag_list()
    assert response["result"] == "ok"
    assert isinstance(response["data"], list)
    assert all("id" in t and "name" in t for t in response["data"])
