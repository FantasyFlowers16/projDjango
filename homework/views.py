# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': [
                    {
                        'id': 1,
                        'fio': 'Иванов Сергей Сергеевич',
                        'python': 4,
                        'java': 5,
                        'javaScript': 4,
                        'php': 5,
                        'sql': 4,
                        'average': 2.4,
                    },
                    {
                        'id': 2,
                        'fio': 'Исакова Людмила Сергеевна',
                        'python': 3,
                        'java': 3,
                        'javaScript': 4,
                        'php': 3,
                        'sql': 2.3,
                        'average': 2.3,
                    },
                    {
                        'id': 3,
                        'fio': 'Гармошкин Иван Павлович',
                        'python': 5,
                        'java': 5,
                        'javaScript': 5,
                        'php': 5,
                        'sql': 5,
                        'average': 2.3,
                    },
                    {
                        'id': 4,
                        'fio': 'Куницына Лидия Николаевна',
                        'python': 2,
                        'java': 3,
                        'javaScript': 2,
                        'php': 2,
                        'sql': 2.3,
                        'average': 2.3,
                    },
                ],
                'excellent_students': 'Student A, Student B',
                'bad_students': 'Student C, Student D'
            }
        )
        return context


class Student:
    pass


class Statistics:
    # student_id, [Scores]
    pass

class Subject:
    pass

class Score:
    # Subject, Student, value
    pass
