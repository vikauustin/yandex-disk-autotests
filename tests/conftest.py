import uuid

import pytest

from disk_api import config
from disk_api.client import DiskClient


@pytest.fixture
def client():
    return DiskClient(config.get_token())


@pytest.fixture
def work_dir(client):
    path = f"{config.TEST_ROOT}/test-{uuid.uuid4().hex[:8]}"
    client.create_folder(config.TEST_ROOT)
    client.create_folder(path)
    yield path
    client.delete(path, permanently=True)