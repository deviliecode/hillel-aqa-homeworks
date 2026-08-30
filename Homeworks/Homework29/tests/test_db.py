import pytest

from db import (
    get_connection,
    create_table,
    insert_result,
    update_result,
    delete_result,
    select_all_results,
    select_result_by_id,
)


@pytest.fixture()
def connection():
    """Фікстура, яка створює підключення і чистить таблицю до/після тесту."""
    conn = get_connection()
    create_table(conn)
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM results;")
    conn.commit()

    yield conn

    conn.close()


def test_connection_is_alive(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1;")
        assert cursor.fetchone()[0] == 1


def test_insert_record(connection):
    record_id = insert_result(connection, name="test_insert", value=10)
    row = select_result_by_id(connection, record_id)

    assert row is not None
    assert row["name"] == "test_insert"
    assert row["value"] == 10


def test_update_record(connection):
    record_id = insert_result(connection, name="test_update", value=5)

    update_result(connection, record_id, value=99)
    row = select_result_by_id(connection, record_id)

    assert row["value"] == 99


def test_delete_record(connection):
    record_id = insert_result(connection, name="test_delete", value=1)

    delete_result(connection, record_id)
    row = select_result_by_id(connection, record_id)

    assert row is None


def test_select_all_records(connection):
    insert_result(connection, name="first", value=1)
    insert_result(connection, name="second", value=2)

    rows = select_all_results(connection)

    assert len(rows) == 2
    names = [row["name"] for row in rows]
    assert "first" in names
    assert "second" in names