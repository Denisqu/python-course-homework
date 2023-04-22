# DONE


#todo: Заданы два списка. Необходимо их сериализовать в один файл.

import pickle

list_one = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
list_two = [False, 'Sparse is better than dense.', {'age': 90}]



fd = open("data_task35.pkl", "wb")
pickle.dump([list_one, list_two], fd, pickle.HIGHEST_PROTOCOL)
fd.close()