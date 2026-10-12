from disk_api.client import DiskClient

def test_request_without_token_returns_401():
    client = DiskClient()

    response = client.get_disk_info()

    assert response.status_code == 401


def test_request_with_invalid_token_returns_401():
    client = DiskClient("invalid-token-123")

    response = client.get_disk_info()

    assert response.status_code == 401