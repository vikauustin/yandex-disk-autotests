def test_get_disk_info_returns_200(client):
    response = client.get_disk_info()
    assert response.status_code == 200

def test_get_disk_info_has_correct_fields(client):
    response = client.get_disk_info()

    info = response.json()
    assert info["total_space"] > 0
    assert info["used_space"] <= info["total_space"]
    assert info["user"]["login"] != ""