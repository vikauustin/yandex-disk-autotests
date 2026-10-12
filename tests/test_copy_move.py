def test_copy_folder(client, work_dir):
    source = f"{work_dir}/source"
    target = f"{work_dir}/copy"
    client.create_folder(source)

    response = client.copy(source, target)

    assert response.status_code in (201, 202)
    assert client.get_resource(source).status_code == 200
    assert client.get_resource(target).status_code == 200


def test_move_folder(client, work_dir):
    source = f"{work_dir}/old"
    target = f"{work_dir}/new"
    client.create_folder(source)

    response = client.move(source, target)

    assert response.status_code in (201, 202)
    assert client.get_resource(source).status_code == 404
    assert client.get_resource(target).status_code == 200