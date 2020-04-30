# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView

data_student = {}


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        student = Student('Petr', 123)
        context.update(
            {
                'students_statistics': [data_student],

                'excellent_students': 'Student A, Student B',
                'bad_students': 'Student C, Student D'
            }
        )
        return context


class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def add_student(self):
        global data_student
        data_student["id"] = self.id
        data_student["fio"] = self.name
        print(data_student)

class Statistics:
    pass


class Subject:
    def __init__(self, python=5, java=5, java_script=5, php=5, sql=5):
        self.python = python
        self.java = java
        self.java_script = java_script
        self.php = php
        self.sql = sql

    def add_subject(self):
        data_student["python"] = self.python
        data_student["java"] = self.java
        data_student["java_script"] = self.java_script
        data_student["php"] = self.php
        data_student["sql"] = self.sql
        data_student["average"] = (self.python + self.java + self.java_script + self.php + self.sql) / 5
        print(data_student)

class Score:
    def __init__(self, data_student):
        middle_point = 0

    # Subject, Student, value
    pass


stud1 = Student("Петров Алексей Сергеевич", 12)
stud1.add_student()
sub1=Subject(4,4,2,4,4)
sub1.add_subject()
stud2 = Student("Иваненко Виталий Гавриловия", 12)
stud2.add_student()
sub2=Subject(2,2,5,5,3)
sub2.add_subject()