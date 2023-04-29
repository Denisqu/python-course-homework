
import io
import os

def get_file(file_name):
    try:
        current_dir = os.getcwd()
        files = os.listdir(current_dir)
        if file_name not in files:
            raise Exception("Файл с таким именем не найден! :(")
    except Exception as e:
        print(e)
    else:
        with io.open(file_name, mode="r", encoding="utf-8") as file:
            print(file.read())



get_file("text.txt")
get_file("OOOOOOOOOO.ooooooo")