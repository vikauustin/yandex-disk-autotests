import requests
import allure
from disk_api import config

class DiskClient:
    def __init__(self, token=None):
        self.session = requests.Session()
        self.session.headers["Accept"] = "application/json"
        if token:
            self.session.headers["Authorization"] = f"OAuth {token}"

    def _request(self, method, endpoint, **kwargs):
        url = config.BASE_URL + endpoint
        return self.session.request(method, url, timeout=30, **kwargs)

    @allure.step("Получить информацию о диске")
    def get_disk_info(self):
        return self._request("GET", "")

    @allure.step("Создать папку {path}")
    def create_folder(self, path):
        return self._request("PUT", "/resources", params={"path": path})

    @allure.step("Удалить {path}")
    def delete(self, path, permanently=False):
        return self._request(
            "DELETE", "/resources",
            params={"path": path, "permanently": str(permanently).lower()},
        )
    
    @allure.step("Получить информацию о ресурсе {path}")
    def get_resource(self, path):
        return self._request("GET", "/resources", params={"path": path})

    @allure.step("Скопировать {from_path} в {path}")
    def copy(self, from_path, path, overwrite=False):
        return self._request(
            "POST", "/resources/copy",
            params={"from": from_path, "path": path, "overwrite": str(overwrite).lower()},
        )

    @allure.step("Переместить {from_path} в {path}")
    def move(self, from_path, path, overwrite=False):
        return self._request(
            "POST", "/resources/move",
            params={"from": from_path, "path": path, "overwrite": str(overwrite).lower()},
        )