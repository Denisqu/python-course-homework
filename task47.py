# todo:
#   Создайте класс Pet с атрибутам имя, вес и уровень сытости.
#   Напишите метод info, который в качестве результата выдает эти атрибуты.
#   Напишите метод hungry, который возвращает уровень сытости и комментирует: если меньше 5, то «голоден», если больше 10, то «сыт».
#   Напишите метод feed, который передает питомцу некоторую еду, которая прибавляется к уровню сытости и вызывает метод info.


class Pet:
    def __init__(self, name, weight, satiety):
        self.__name = name
        self.__weight = weight
        self.__satiety = satiety

    def info(self):
        print(f"name = {self.__name}, weight = {self.__weight}, satiety = {self.__satiety}")

    def hungry(self):
        if self.__satiety < 5:
            print("hungry...")
        elif self.__satiety > 10:
            print("Full! :-)")
        return self.__satiety

    def feed(self, food):
        self.__satiety += food
        self.info()



a = Pet("Cat", 10, 4)
print(a.hungry())
a.feed(11)
print(a.hungry())
