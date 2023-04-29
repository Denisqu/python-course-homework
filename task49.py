# todo:
#  Определите класс Person. В конструктор которого передается фамилия и возраст ('Иванов', 29)
#  Реализуйте через магические методы условие, при котором возраст у объекта не будет меняться после инициализации.

class Person:
    def __init__(self, surname, age):
        self.surname = surname
        self.age = age

    def __setattr__(self, attr, value):
        if attr != 'age' or self.__dict__.get(attr) is None:
            self.__dict__[attr] = value
        else:
            print("changing of this attribute is not allowed!!!")


p = Person("Ivanov", 29)
p.age = 11111
p.surname = "Petrov"

print(f"{p.surname} : {p.age}")