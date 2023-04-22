import pickle
import json
import yaml


# # Функция десериализует объект из файла типа pickle
# # file - файл для десериализации к примеру "data.pkl"
def from_pickle(file):
    return pickle.load(file)


# # Функция десериализует объект из файла типа json
# # from_json - функция сереализует объект в json
# # Параметры
# # file - файл для десериализации к примеру "data.json"
def from_json(file):
    return json.load(file)


# # Функция десериализует объект из файла типа yaml
# # Параметры
# # file - файл для десериализации к примеру "data.yml"
def from_yaml(file):
    return yaml.load(file, Loader=yaml.Loader)
