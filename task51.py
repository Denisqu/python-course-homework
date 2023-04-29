#todo:
# Определите класс Person. При создании объекта p=Person(‘Иванов’, ‘Михаил’, ‘Федорович’) необходимо ввести полное имя человека.
# При печати объекта должно выводиться следующее:
# print(p) # чивородеФлиахиМвонавИ

class Person:
    def __init__(self, surname, name, patronymic_surname):
        self.__surname = surname
        self.__name = name
        self.__patronymic_surname = patronymic_surname

    def __repr__(self):
        return f"{self.__surname}{self.__name}{self.__patronymic_surname}"[::-1]

p = Person('Иванов', 'Михаил', 'Федорович')
print(p)
