# todo:
#  Создайте класс Triangle с методом, который при создании объекта проверяет три переменный x, y, z на то,
#  что из них можно составить треугольник. Требования: все числа должны быть больше нуля, сумма любых двух должны быть больше третьего.

class Triangle:
    def _can_construct(self, x, y, z):
        if x <= 0 or y <= 0 or z <= 0:
            return False
        if x + y <= z and x + z <= y and y + z <= x:
            return False
        return True


    def __init__(self, x, y, z):
        if self._can_construct(x, y, z):
            __x = x
            __y = y
            __z = z
        else:
            print("can't construct!")
