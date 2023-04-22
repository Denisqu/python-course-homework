# #todo 1: создайте модуль serializer
#
# # В модуле реализуйте три функции сериализации
#
# # Функция сериализует объект в байтовый поток pickle
# # Параметры
# # obj - сериализуемый объект
# # file - файл для сериализации к примеру "data.pkl"

import pickle
import json
import yaml


def to_pickle(obj, file):
    pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)
    


#
# #  Функция сериализует объект в json
# #  Параметры
# # obj - сериализуемый объект
# # file - файл для сериализации к примеру "data.json"


def to_json(obj, file):
    json.dump(obj, file, indent=4)



# # Функция сериализует объект в yaml
# # Параметры
# # obj - сериализуемый объект
# # file - файл для сериализации к примеру "data.yml"


def to_yaml(obj, file):
    yaml.dump(obj, file, Dumper=yaml.Dumper)
    

