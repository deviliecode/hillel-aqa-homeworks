# Генератори:
# 1. Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
import logging

print("--- Завдання 1.1 ---")
def generator_parnyh(n):
    current = 0
    for i in range(n // 2):
        current += 2
        if current > n:
            return
        yield current

for j in generator_parnyh(10):
    print(j)

# 2. Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
print("--- Завдання 1.2 ---")
def fi_generator(n):
    first_num = 1
    second_num = 1
    while first_num <= n:
        yield first_num
        old_first = first_num
        first_num = second_num
        second_num = old_first + second_num

for fi in fi_generator(1000):
    print(fi)


# Ітератори:
# 1. Реалізуйте ітератор для зворотного виведення елементів списку.
print("--- Завдання 2.1 ---")
class ShowReverseItems:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lst[self.index]

for i in ShowReverseItems([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(i)

# 2. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
print("--- Завдання 2.2 ---")
class ParniNumbers:
    def __init__(self, num):
        self.num = num
        self.current = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.num:
            raise StopIteration
        return self.current

for k in ParniNumbers(8):
    print(k)


# Декоратори:
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
print("--- Завдання 3.1 ---")
def log_decorator(func):
    def wrapper(*args):
        result = func(*args)
        print(f"Функція {func.__name__} виконалась з результатом: {result}, з доданками: {args}")
        return result
    return wrapper

@log_decorator
def add(x, y):
    return x + y

print(add(5, 5))

# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
print("--- Завдання 3.2 ---")
def exception_handler(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as e:
            print(f"Помилка в {func.__name__}: {e}")
            return None
    return wrapper

@exception_handler
def divide(a, b):
    return a / b

print(divide(10, 0))
