#todo: Задача 1 Переопределите метод __str__, чтобы в нем печатались все атрибуты объекта и их значения через запятую. Например:
# def __init__(self):
#     self.x = 0
#     self.y = 1
#
# Должно быть напечатано x:0, y:1


class Foo:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.asdaosdwqo = 129124124

    def __str__(self):
        lst = [f"{i}:{j}, " for i,j in self.__dict__.items()]
        my_str = ""
        for i in lst:
            my_str += i
        return my_str[:-2]


print(Foo().__str__())