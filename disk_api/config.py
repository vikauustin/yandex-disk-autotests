import os

BASE_URL = "https://cloud-api.yandex.net/v1/disk"

TEST_ROOT = "disk:/autotests"

def get_token():
    return os.getenv("YANDEX_DISK_TOKEN", "").strip()