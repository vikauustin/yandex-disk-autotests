import allure

@allure.feature("Папки")
@allure.title("Создание папки возвращает 201")
def test_create_folder_returns_201(client, work_dir):
    response = client.create_folder(f"{work_dir}/new")

    assert response.status_code == 201

@allure.feature("Папки")
@allure.title("Созданная папка имеет корректные метаданные: тип dir и верное имя")
def test_created_folder_has_correct_meta(client, work_dir):
    path = f"{work_dir}/meta"
    client.create_folder(path)

    response = client.get_resource(path)

    assert response.status_code == 200
    assert response.json()["type"] == "dir"
    assert response.json()["name"] == "meta"

@allure.feature("Папки")
@allure.title("Повторное создание папки возвращает 409")
def test_create_existing_folder_returns_409(client, work_dir):
    path = f"{work_dir}/twice"
    client.create_folder(path)

    response = client.create_folder(path)

    assert response.status_code == 409
    assert response.json()["error"] == "DiskPathPointsToExistentDirectoryError"

@allure.feature("Папки")
@allure.title("Получение несуществующей папки возвращает 404")
def test_get_missing_folder_returns_404(client, work_dir):
    response = client.get_resource(f"{work_dir}/no-such-folder")

    assert response.status_code == 404