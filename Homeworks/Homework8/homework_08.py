class Student:

    def __init__(s, first_name, second_name, age: int, avarage_score):
        s.first_name = first_name
        s.second_name = second_name
        s.age = age
        s.avarage_score = avarage_score

    def change_avarage_score(s, new_avarage_score: int):
        s.avarage_score = new_avarage_score
        return s.avarage_score


yaroslav = Student("Yaroslav", "Faliush", 22, 92)

print(f"Ім'я студента: {yaroslav.first_name}, прізвище студента: {yaroslav.second_name}, вік студента: {yaroslav.age}, середній бал: {yaroslav.avarage_score}")
yaroslav.change_avarage_score(95)
print(f"Новий середній бал студента {yaroslav.first_name} —— {yaroslav.avarage_score}")