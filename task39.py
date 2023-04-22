# DONE

# #todo 1: создайте модуль serializer
#
# # В модуле реализуйте три функции сериализации
#
# # Функция сериализует объект в байтовый поток pickle
# # Параметры
# # obj - сериализуемый объект
# # file - файл для сериализации к примеру "data.pkl"
# def to_pickle(obj, file):
#     pass
#     # ваш код
#
# #  Функция сериализует объект в json
# #  Параметры
# # obj - сериализуемый объект
# # file - файл для сериализации к примеру "data.json"
# def to_json(obj, file):
#     pass
#     # ваш код
#
# # Функция сериализует объект в yaml
# # Параметры
# # obj - сериализуемый объект
# # file - файл для сериализации к примеру "data.yml"
# def to_yaml(obj, file):
#     pass
#     # ваш код
#
#
# #todo 2: Cоздайте модуль deserializer. В модуле реализуйте три функции десериализации
#
#
# # Функция десериализует объект из файла типа pickle
# # file - файл для десериализации к примеру "data.pkl"
# def from_pickle(file):
#     pass
#     # ваш код
#
# # Функция десериализует объект из файла типа json
# # from_json - функция сереализует объект в json
# # Параметры
# # file - файл для десериализации к примеру "data.json"
# def from_json(file):
#     pass
#     # ваш код
#
#
# # Функция десериализует объект из файла типа yaml
# # Параметры
# # file - файл для десериализации к примеру "data.yml"
# def from_yaml(file):
#     pass
#     # ваш код
#
# #todo 3: Cоздайте пакет из двух модулей serializer и deserializer.
#
# # Импортируйте модули пакета в отдельный файл и протестируйте все функции.
from myserializer import serializer, deserializer
test_data_to_serialize = ["this is a test data", {"what data is it?": "it is a test data!", "Meaning of life": 42}]

with open("data.pkl", "wb") as file:
    serializer.to_pickle(test_data_to_serialize, file)
with open("data.pkl", "rb") as file:
    print(deserializer.from_pickle(file))

with open("data.json", "wt") as file:
    serializer.to_json(test_data_to_serialize, file)
with open("data.json", "rt") as file:
    print(deserializer.from_json(file))

with open("data.yaml", "wt") as file:
    serializer.to_yaml(test_data_to_serialize, file)
with open("data.yaml", "rt") as file:
    print(deserializer.from_yaml(file))


