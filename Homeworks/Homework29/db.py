import os
import time

import psycopg2
from psycopg2.extras import RealDictCursor


DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "dbname": os.getenv("DB_NAME", "app_db"),
    "user": os.getenv("DB_USER", "app_user"),
    "password": os.getenv("DB_PASSWORD", "app_password"),
}


def get_connection(retries: int = 10, delay: int = 2):
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            connection = psycopg2.connect(**DB_CONFIG)
            return connection
        except psycopg2.OperationalError as error:
            last_error = error
            print(f"Спроба {attempt}/{retries}: БД ще не готова, чекаємо {delay}с...")
            time.sleep(delay)
    raise ConnectionError(f"Не вдалося підключитися до БД: {last_error}")


def create_table(connection) -> None:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS results (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                value INTEGER NOT NULL
            );
            """
        )
    connection.commit()


def insert_result(connection, name: str, value: int) -> int:
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO results (name, value) VALUES (%s, %s) RETURNING id;",
            (name, value),
        )
        new_id = cursor.fetchone()[0]
    connection.commit()
    return new_id


def update_result(connection, record_id: int, value: int) -> None:
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE results SET value = %s WHERE id = %s;",
            (value, record_id),
        )
    connection.commit()


def delete_result(connection, record_id: int) -> None:
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM results WHERE id = %s;", (record_id,))
    connection.commit()


def select_all_results(connection) -> list:
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT * FROM results ORDER BY id;")
        return cursor.fetchall()


def select_result_by_id(connection, record_id: int):
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT * FROM results WHERE id = %s;", (record_id,))
        return cursor.fetchone()