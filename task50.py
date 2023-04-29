# DONE

#todo
# Создайте декоратор, которые переводит все текстовые аргументы функции в верхний регистр и возвращает их в виде списка текстовых аргументов.

def decorator(func):
    def wrapper(*args, **kwargs):
        _args = [i.upper() for i in args]
        _kwargs = {k:v.upper() for k, v in kwargs.items()}
        func(*_args, **_kwargs)
        return _args + list(_kwargs.values())
    return wrapper

@decorator
def f0(a, b, c, named_var = "vAr_nAme"):
    print(a, b, c, named_var)

lst = f0("0", "asddAD", "asdads", named_var = "var_name")
print(lst)