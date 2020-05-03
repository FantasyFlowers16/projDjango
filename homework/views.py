# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView

data_student = {}
all_data_student = []


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        student = Student('Petr', 123)
        context.update(
            {
                'students_statistics': all_data_student,

                'excellent_students': 'Student A, Student B',
                'bad_students': 'Student C, Student D'
            }
        )
        return context


class Student:
    def __init__(self, name, id, subject=0):
        self.name = name
        self.id = id
        self.subject = subject

    def add_student(self):
        data_student = {}
        data_student["id"] = self.id
        data_student["fio"] = self.name
        all_data_student.append(data_student)
        return data_student


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
        data_student = {}
        data_student["python"] = self.python
        data_student["java"] = self.java
        data_student["java_script"] = self.java_script
        data_student["php"] = self.php
        data_student["sql"] = self.sql
        data_student["average"] = (self.python + self.java + self.java_script + self.php + self.sql) / 5
        return data_student


    def union_data(self, data_st,data_student):
        data_st.update(data_student)
        print(data_st)


class Score:
    def __init__(self, all_data_student):
        middle_point = 0

    # Subject, Student, value
    pass

#Добавление студентов
stud1 = Student("Петров Алексей Сергеевич", 9212)
sub1 = Subject(4, 4, 2, 4, 4)
sub1.union_data(stud1.add_student(),sub1.add_subject())

stud1 = Student("Заикина Юлия Олеговна", 1223)
sub1 = Subject(5, 5, 5, 5, 2)
sub1.union_data(stud1.add_student(),sub1.add_subject())

stud1 = Student("Портнягина Алия Мамбетовна", 2312)
sub1 = Subject(2, 4, 2, 3, 3)
sub1.union_data(stud1.add_student(),sub1.add_subject())

stud1 = Student("Ильин Иван Гамзатович", 2212)
sub1 = Subject(4, 5, 5, 4, 5)
sub1.union_data(stud1.add_student(),sub1.add_subject())

stud1 = Student("Кариманов Ашот ОТолбекович", 6812)
sub1 = Subject(2, 2, 2, 3, 2)
sub1.union_data(stud1.add_student(),sub1.add_subject())