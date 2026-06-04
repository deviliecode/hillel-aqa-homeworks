class Student:

    def __init__(self, first_name, second_name, age: int, avarage_score):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.avarage_score = avarage_score

    def change_avarage_score(self, new_avarage_score: int):
        self.avarage_score = new_avarage_score


yaroslav = Student("Yaroslav", "Faliush", 22, 92)

print(f"Ім'я студента: {yaroslav.first_name}, прізвище студента: {yaroslav.second_name}, вік студента: {yaroslav.age}, середній бал: {yaroslav.avarage_score}")
yaroslav.change_avarage_score(95)
print(f"Новий середній бал студента {yaroslav.first_name} —— {yaroslav.avarage_score}")