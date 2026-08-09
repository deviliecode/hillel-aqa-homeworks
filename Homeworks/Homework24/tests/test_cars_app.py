import logging
import pytest
import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("BASE_URL_24")

#Налаштування логування
logger = logging.getLogger("test_search")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("Homeworks/Homework24/tests/test_search.log")
console_handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


class TestCarsSearch:

    @pytest.mark.parametrize(
        "sort_by, limit, expected_brands",
        [
            # 5 найдешевших авто за ціною
            ("price", 5, ["Chevrolet", "Hyundai", "Honda", "Kia", "Ford"]),

            # 3 найстаріші авто за роком випуску
            ("year", 3, ["Ford", "Honda", "Toyota"]),

            # перші 10 марок за алфавітом
            ("brand", 10, [
                "Acura", "Audi", "BMW", "Bugatti", "Chevrolet",
                "Ferrari", "Ford", "Honda", "Hyundai", "Infiniti"
            ]),

            # 4 авто з найменшим об'ємом двигуна
            ("engine_volume", 4, ["Tesla", "Nissan", "Honda", "Hyundai"]),

            # найдешевше авто
            ("price", 1, ["Chevrolet"]),

            # sort_by не задано -> сервер сортує за замовчуванням по brand
            (None, 7, [
                "Acura", "Audi", "BMW", "Bugatti",
                "Chevrolet", "Ferrari", "Ford"
            ]),
        ]
    )
    def test_cars_search(self, auth_session, sort_by, limit, expected_brands):
        params = {"limit": limit}
        if sort_by:
            params["sort_by"] = sort_by

        logger.info("Відправляємо GET /cars з параметрами: %s", params)

        response = auth_session.get(f"{base_url}/cars", params=params)

        logger.info("Отримано статус код: %s", response.status_code)

        assert response.status_code == 200

        cars = response.json()

        logger.info("Кількість отриманих автомобілів: %s", len(cars))

        #перевіряємо, що кількість автомобілів відповідає limit
        assert len(cars) == limit

        #порівнюємо марки авто у відповіді з тими, що ми очікували
        actual_brands = [car["brand"] for car in cars]

        logger.info("Отримані марки: %s", actual_brands)
        logger.info("Очікувані марки: %s", expected_brands)

        assert actual_brands == expected_brands

    def test_cars_search_all_sorted_by_year(self, auth_session):
        """
        Окремий тест на весь список (limit=25), без пофіксованих марок.
        Перевіряємо кількість авто і те, що список дійсно відсортований
        за роком, а також знаємо, яке авто має бути першим і останнім.
        """
        params = {"sort_by": "year", "limit": 25}

        logger.info("Відправляємо GET /cars з параметрами: %s", params)

        response = auth_session.get(f"{base_url}/cars", params=params)

        assert response.status_code == 200

        cars = response.json()

        logger.info("Кількість отриманих автомобілів: %s", len(cars))

        #у базі всього 25 авто, тому очікуємо повний список
        assert len(cars) == 25

        #перевіряємо, що роки йдуть за зростанням
        years = [car["year"] for car in cars]
        assert years == sorted(years)

        #ми знаємо, що найстаріше авто в базі - Ford (2015 рік)
        assert cars[0]["brand"] == "Ford"

        #а останнє авто у списку (серед машин 2021 року) - McLaren
        assert cars[-1]["brand"] == "McLaren"

        logger.info("Повний список коректно відсортований за роком")