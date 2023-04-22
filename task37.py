# DONE


#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

from datetime import datetime

log_counter = dict()
def call_logger_decorator(func):
    def wrapper(*args, **kwargs):
        call_time = datetime.now()
        value = log_counter.get(func.__name__, [0, ""])
        value[0] += 1
        value[1] = str(call_time)
        log_counter[func.__name__] = value

        func(*args, **kwargs)
    return wrapper

def update_log():
    with open("debug.log", "a") as file_object:
        for key, value in log_counter.items():
            file_object.write(f"{key}, {value[0]}, {value[1]}\n")



@call_logger_decorator
def f1():
    pass

@call_logger_decorator
def f2():
    pass


f1()
f1()
f1()
f2()
f2()
f1()
print(log_counter)
update_log()




