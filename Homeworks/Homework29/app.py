from db import get_connection, create_table, insert_result, select_all_results


def process_data(numbers: list[int]) -> int:
    return sum(numbers)

def main():
    connection = get_connection()
    try:
        create_table(connection)

        numbers = [1, 2, 3, 4, 5]
        result = process_data(numbers)
        record_id = insert_result(connection, name="sum_of_numbers", value=result)
        print(f"Збережено результат: id={record_id}, value={result}")

        print("Усі записи в базі:")
        for row in select_all_results(connection):
            print(row)
    finally:
        connection.close()

if __name__ == "__main__":
    main()