# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def multiplication_table(number):
    multiplier = 1
    while multiplier:
        result = number * multiplier
        if  result > 25:
            break
        elif multiplier > 10:
            break

        print(f"{number}x{multiplier}={result}")

        multiplier += 1

print("# task 1")
multiplication_table(7)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def add(x, y):
    return x + y

print(f"\n# task 2\n{add(5, 4)}\n")


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic(list_1):
    total = 0
    for i in list_1:
        total += i
    return total / len(list_1)

print(f"# task 3\nСереднє арифметичне списку чисел — {arithmetic([11, 3, 6, 7, 20, 499])}\n")


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse(str_1):
    list_1 = []
    for i in str_1[::-1]:
        list_1.append(i)
    return "".join(list_1)
print(f"# task 4\nПеревернутий рядок —— {reverse('Mama')}\n")


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def find_longest_word(words):
    longest = words[0]
    for i in words[1:]:
        if len(i) > len(longest):
            longest = i
    return longest
print(f"# task 5\nНайдовше слово —— {find_longest_word(['Hellll', 'Mama', 'Yaroslav', 'Pizza', 'Haisenberg', 'Schwiztherland'])}\n")


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    for i in range(len(str1) - len(str2) + 1):
        if str1[i:i + len(str2)] == str2:
            return i
    return -1

str1 = "Hello, world!"
str2 = "world"
print(f"# task 6")
print(f"Індекс першого входження другого рядка у перший рядок —— {find_substring(str1, str2)}")

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))


# task 7
print(f"\n# task 7")
def string_item_count(lst):
    """Функція з домашки 6.3 —— рахує скільки у списку елементів з типм str"""
    lst2 = []
    for i in lst:
        if type(i) == str:
            lst2.append(i)

    if lst2:
        print(f"Список lst2 має {len(lst2)} елементів з типом str")
    else:
        print("Список lst2 НЕмає змінних з типом str")

string_item_count(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])

# task 8
print(f"\n# task 8")
def count_parni(lst):
    """Функція з допмшки 6.5 —— рахує кількість парних чисел у списку"""
    parni = []
    for i in lst:
        if i % 2 == 0:
            parni.append(i)
    print(f"Парних чисел —— {len(parni)}")

count_parni([1, 3, 4, 123, 4, 32, 33, 32, 15, 13, 2000, 2001])


# task 9
print(f"\n# task 9")
def sum_square_sea(first_sea, second_sea):
    """Функція з домашки 3 —— рахує суму площ обох морів"""
    sum_square = first_sea + second_sea
    print(f"Загальна полща обох морів становить —— {sum_square}\n")

sum_square_sea(436402, 37800)


# task 10
print(f"# task 10")
def count_computer_price(month_count, money_per_month):
    total_cost = month_count * money_per_month
    print(f"Вартість комп'ютера —— {total_cost} грн.\n")

count_computer_price(18, 1179)


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""