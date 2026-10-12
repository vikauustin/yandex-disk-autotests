import requests

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

    def get_disk_info(self):
        return self._request("GET", "")

    def create_folder(self, path):
        return self._request("PUT", "/resources", params={"path": path})

    def delete(self, path, permanently=False):
        return self._request(
            "DELETE", "/resources",
            params={"path": path, "permanently": str(permanently).lower()},
        )
    
    def get_resource(self, path):
        return self._request("GET", "/resources", params={"path": path})

    def copy(self, from_path, path, overwrite=False):
        return self._request(
            "POST", "/resources/copy",
            params={"from": from_path, "path": path, "overwrite": str(overwrite).lower()},
        )

    def move(self, from_path, path, overwrite=False):
        return self._request(
            "POST", "/resources/move",
            params={"from": from_path, "path": path, "overwrite": str(overwrite).lower()},
        )