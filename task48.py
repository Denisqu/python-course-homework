# todo:
#  Создайте класс Shape, объекты которого имеют атрибуты
#  Colour – строка, например, «Красный», «Синий»;
#  Square – площадь объекта.
#  Создайте несколько методов:
#  1) Установить цвет объекта.
#  2) Запросить цвет объекта и напечатать его.
#  3) Задать площадь объекта.
#  4) Запросить площадь  объекта.

class Shape:
    def __init__(self):
        self.__colour = ""
        self.__square = 0

    @property
    def colour(self):
        print(f"Colour of object is {self.__colour}")
        return self.__colour

    @colour.setter
    def colour(self, val):
        self.__colour = val

    def set_square(self, val):
        self.__square = val

    def get_square(self):
        return self.__square


a = Shape()
a.colour = "red"
print(a.colour)
a.set_square(100)
print(a.get_square())
