# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView

all_data_student = []


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': all_data_student,
                'excellent_students': (', '.join(exellent_student)),
                'bad_students': (', '.join(bad_student))
            }
        )
        return context


class Student:
    def __init__(self, name, id, subject=0):
        self.name = name
        self.id = id
        self.subject = subject

    def add_student(self):
        data_student = {"id": self.id, "fio": self.name}
        all_data_student.append(data_student)
        return data_student


class Subject:
    def __init__(self, python=5, java=5, java_script=5, php=5, sql=5):
        self.python = python
        self.java = java
        self.java_script = java_script
        self.php = php
        self.sql = sql

    def add_subject(self):
        data_student = {"python": self.python, "java": self.java, "java_script": self.java_script, "php": self.php,
                        "sql": self.sql,
                        "average": (self.python + self.java + self.java_script + self.php + self.sql) / 5}
        return data_student

    def union_data(self, data_st, data_student):
        data_st.update(data_student)


class Statistics:
    def bad_student(self):
        all_average = sorted([student['average'] for student in all_data_student])
        print(all_average)

        for student in all_data_student:
            if student['average'] is all_average[0]:
                bad_student_1 = student['fio']
            if student['average'] is all_average[1]:
                bad_student_2 = student['fio']

        # bad_student_1=[student['fio'] for student in all_data_student if student['average'] is all_average[0]]
        # bad_student_2 =[student['fio'] for student in all_data_student if student['average'] is all_average[1]]
        return bad_student_1, bad_student_2

    def exellent_student(self):
        all_average = sorted([student['average'] for student in all_data_student])

        for student in all_data_student:
            if student['average'] is all_average[-1]:
                exellent_student_1 = student['fio']
            if student['average'] is all_average[-2]:
                exellent_student_2 = student['fio']

        # exellent_student_1 = [student['fio'] for student in all_data_student if student['average'] is all_average[-1]]
        # exellent_student_2 = [student['fio'] for student in all_data_student if student['average'] is all_average[-2]]

        return exellent_student_1, exellent_student_2


# Добавление студентов
stud1 = Student("Петров Алексей Сергеевич", 9212)
sub1 = Subject(4, 4, 2, 4, 4)
sub1.union_data(stud1.add_student(), sub1.add_subject())

stud1 = Student("Заикина Юлия Олеговна", 1223)
sub1 = Subject(5, 5, 5, 5, 2)
sub1.union_data(stud1.add_student(), sub1.add_subject())

stud1 = Student("Портнягина Алия Мамбетовна", 2312)
sub1 = Subject(2, 4, 2, 3, 3)
sub1.union_data(stud1.add_student(), sub1.add_subject())

stud1 = Student("Ильин Иван Гамзатович", 2212)
sub1 = Subject(4, 5, 5, 4, 5)
sub1.union_data(stud1.add_student(), sub1.add_subject())

stud1 = Student("Кариманов Ашот Отолбекович", 6812)
sub1 = Subject(2, 3, 5, 3, 4)
sub1.union_data(stud1.add_student(), sub1.add_subject())

stud1 = Student("Казанов Евгений Леонидович", 4713)
sub1 = Subject(2, 2, 2, 2, 2)
sub1.union_data(stud1.add_student(), sub1.add_subject())

stud1 = Student("Сарычева Елена Константиновна", 5479)
sub1 = Subject(5, 4, 5, 5, 5)
sub1.union_data(stud1.add_student(), sub1.add_subject())

# Добавление лучших и худших
st = Statistics()
bad_student = st.bad_student()
exellent_student = st.exellent_student()
