# Test cases for the /legacy/mapping endpoint (stub/mock)

def test_legacy_mapping():
    """Test legacy ID mapping (stub/mock)"""
    class DummyClient:
        def legacy_mapping(self, ids):
            return {"result": "ok", "data": [{"legacyId": i, "newId": f"new-{i}"} for i in ids]}
    client = DummyClient()
    response = client.legacy_mapping(["old-1", "old-2"])
    assert response["result"] == "ok"
    assert isinstance(response["data"], list)
    assert all("legacyId" in m and "newId" in m for m in response["data"])
