import random

from db import session
from data_models import Student, Course


#Створення моделі даних: 5 курсів і 20 студентів
course_names = [
    "Python Basics",
    "Manual QA",
    "Test Automation",
    "SQL for Testers",
    "API Testing",
]

courses_list = []
for i in course_names:
    new_course = Course(title=i)
    courses_list.append(new_course)
    session.add(new_course)

students_list = []
for i in range(1, 21):
    new_student = Student(name=f"Student {i}", email=f"student{i}@example.com")
    students_list.append(new_student)
    session.add(new_student)

session.commit()

for student in students_list:
    how_many_courses = random.randint(1, 3)
    random_courses = random.sample(courses_list, how_many_courses)
    for course in random_courses:
        student.courses.append(course)

session.commit()
print("Створено 5 курсів та 20 студентів, курси розподілено випадково.\n")


#Базові операції: додаємо нового студента і записуємо на курс
new_student = Student(name="Student Yaroslav", email="new.student@example.com")

api_course = session.query(Course).filter_by(title="API Testing").first()
new_student.courses.append(api_course)

session.add(new_student)
session.commit()

print(f"Додано студента {new_student.name} на курс {api_course.title}\n")


#Запити до бази даних
#Всі студенти, записані на певний курс
print("Студенти на курсі 'API Testing':")
course = session.query(Course).filter_by(title="API Testing").first()
for student in course.students:
    print(f"  - {student.name}")

#Всі курси, на які записаний певний студент
print("Курси студента 'Student 1':")
student = session.query(Student).filter_by(name="Student 1").first()
for course in student.courses:
    print(f"  - {course.title}")


#Оновлення та видалення даних
#Оновлення: змінюємо email студента
student = session.query(Student).filter_by(name="Student 1").first()
student.email = "updated.student1@example.com"
session.commit()
print(f"Email студента Student 1 оновлено на {student.email}")

#Видалення: видаляємо студента з бази даних
student_to_delete = session.query(Student).filter_by(name="Student 2").first()
session.delete(student_to_delete)
session.commit()
print("Студента Student 2 видалено з бази даних")

session.close()