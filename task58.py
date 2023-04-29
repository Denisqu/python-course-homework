# DONE


#todo: Создать абстрактный класс Transport (транспорт) содержащий:
# Поля:
# скорость;
# себестоимость перевозки груза;
# стоимость перевозки груза.
# В классе должны быть абстрактные методы:
# метод Cost (без параметров) – вычисление стоимости перевозки груза.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Marine - морской транспорт,
# Ground - наземный транспорт.

from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, velocity, cost_price):
        self._velocity = velocity
        self._cost_price = cost_price
        self._price = self.cost()

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Ground(Transport):
    def cost(self):
        return self._cost_price * 2

    def info(self):
        return f"Ground transport: v = {self._velocity}, cost = {self._cost_price}"


class Marine(Transport):
    def cost(self):
        return self._cost_price * 3

    def info(self):
        return f"Marine transport: v = {self._velocity}, cost = {self._cost_price}"


m = Marine(100, 1244)
g = Ground(99, 121)

print(m.info(), g.info())