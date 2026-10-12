def test_delete_folder(client, work_dir):
    path = f"{work_dir}/to-delete"
    client.create_folder(path)

    response = client.delete(path, permanently=True)

    assert response.status_code == 204
    assert client.get_resource(path).status_code == 404


def test_delete_missing_folder_returns_404(client, work_dir):
    response = client.delete(f"{work_dir}/no-such-folder", permanently=True)

    assert response.status_code == 404