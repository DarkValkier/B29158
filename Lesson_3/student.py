import datetime


class Student:
    name = ''
    birth_year = 0
    group = ''
    mark = .0

    # Конструктор __init__

    # __str__

    def get_age(self):
        return datetime.date.today().year - self.birth_year
