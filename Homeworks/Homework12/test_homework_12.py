import unittest
from homework_12 import *

class TestSumSquareSea(unittest.TestCase):

    def test_sum_square_sea_positive(self):
        """Тест-кейс хепі пасу рахування площі морів"""
        actual_result = sum_square_sea(436402, 37800)
        expected_result = 474202
        self.assertEqual(actual_result, expected_result)

    def test_sum_square_sea_negative(self):
        """Тест-кейс негативний, очікує помилку якщо один із аргументів стрінга"""
        with self.assertRaises(TypeError):
            sum_square_sea(first_sea=436402, second_sea="37800")

class TestCountParni(unittest.TestCase):

    def test_count_parni_5(self):
        """Тест-кейс перевіряє кількість праних чисел"""
        actual_result = count_parni([2, 4, 6, 8, 10])
        expected_result = 5
        self.assertEqual(actual_result, expected_result)

    def test_count_parni_0(self):
        """Тест-кейс перевіряї відсутність парних чисел"""
        actual_result = count_parni([1, 3, 5, 9, 11])
        expected_result = 0
        self.assertEqual(actual_result, expected_result)

    def test_count_parni_with_zero(self):
        """Тест-кейс що числа 0 не рахуються як парні"""
        actual_result = count_parni([0, 2, 1, 0])
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

class TestStringItemCount(unittest.TestCase):

    def test_string_item_count_only_str(self):
        """Тест-кейс перевіряє кількість стрінгів в списку з тільки стрінгами"""
        actual_result = string_item_count(['1', '2','False','6', 'Python','Lorem Ipsum'])
        expected_result = 6
        self.assertEqual(actual_result, expected_result)

    def test_string_item_count_no_str(self):
        """Тест-кейс перевіряє відсутність стрінгів в списку з тільки числами"""
        actual_result = string_item_count([3, 5, 7, 8, 9, 0])
        expected_result = "Список немає елементів str"
        self.assertEqual(actual_result, expected_result)

    def test_string_item_count_str_and_num(self):
        """Тест-кейс перевіряє кількість стрінгів в списку з різними типами даних"""
        actual_result = string_item_count(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0])
        expected_result = 5
        self.assertEqual(actual_result, expected_result)

class TestCountComputerPrice(unittest.TestCase):

    def test_count_computer_price_positive(self):
        """Тест-кейс перевіряє успішне визначення загальної суми"""
        actual_result = count_computer_price(18, 1000)
        expected_result = 18000
        self.assertEqual(actual_result, expected_result)

    def test_count_computer_price_with_zero(self):
        """Тест-кейс перевіряє що якщо аргумент month_count відсутній, буде підніматись помилка"""
        with self.assertRaises(TypeError):
            count_computer_price(1000)

if __name__ == '__main__':
    unittest.main()