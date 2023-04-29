from abc import ABC, abstractmethod

class Press(ABC):

    def __init__(self, name, price):
        self.price = price
        self.name = name

    @abstractmethod
    def SetPrice(self, price):
        pass

    @abstractmethod
    def Info(self):
        pass

class Magazine(Press):
    def SetPrice(self, price):
        self.price = price + 100

    def Info(self):
        print(f"Magazine info: {self.name}, {self.price}")

class Book(Press):
    def SetPrice(self, price):
        self.price = price + 1

    def Info(self):
        print(f"Book info: {self.name}, {self.price}")

m = Magazine("Мурзилка", 0)
m.SetPrice(100)
m.Info()

b = Book("Война и мир", 0)
b.SetPrice(100)
b.Info()