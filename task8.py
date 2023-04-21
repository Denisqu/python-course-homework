# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".

a = input("enter 4-digit int value")
answer = "YES!" if a == a[::-1] else "NO!"
print(f"a = {a}, is a an palindrome?\n Answer: {answer}")