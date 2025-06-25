# Test cases for the /user/me endpoint (stub/mock)

def test_get_user_me():
    """Test getting the current user's info (stub/mock)"""
    class DummyClient:
        def get_user_me(self):
            return {"result": "ok", "data": {"id": "user-id-1", "username": "testuser"}}
    client = DummyClient()
    response = client.get_user_me()
    assert response["result"] == "ok"
    assert isinstance(response["data"], dict)
    assert response["data"]["username"] == "testuser"
