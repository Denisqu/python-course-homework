# DONE


#todo:
# Реализовать декоратор который подсчитывает время выполнения функции.

from datetime import datetime
import time

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        execution_time = datetime.now() - start_time
        print(f"{func} execution time = {execution_time}")
    return wrapper

@execution_time_decorator
def f(time_to_sleep):
    time.sleep(time_to_sleep)

f(1)
f(0.25)
f(0.5)