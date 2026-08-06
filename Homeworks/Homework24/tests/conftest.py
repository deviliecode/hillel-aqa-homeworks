import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("BASE_URL_24")
username = os.getenv("USERNAME_24")
password = os.getenv("PASSWORD_24")

logger = logging.getLogger("test_search")

@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()

    logger.info("Виконуємо аутентифікацію користувача %s", username)

    response = session.post(f"{base_url}/auth", auth=HTTPBasicAuth(username, password))

    assert response.status_code == 200, "Аутентифікація не пройшла"

    access_token = response.json()["access_token"]
    session.headers.update({"Authorization": "Bearer " + access_token})

    logger.info("Токен доступу отримано, сесія готова до роботи")

    return session