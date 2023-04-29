# Назовем пароль хорошим, если
#
# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра
# Напишите программу, которая требует ввода нового пароля до тех пор, пока не будет введен хороший.
#
#
# На вход программе подается произвольное количество паролей, каждый на отдельной строке. Гарантируется, что среди них присутствует хороший.
#
#
# Для каждого введенного пароля программа должна вывести текст:
#
# LengthError, если длина введенного пароля меньше 9 символов
# LetterError, если в нем все буквы имеют одинаковый регистр
# DigitError, если в нем нет ни одной цифры
# Success!, если введенный пароль хороший
#
# После ввода хорошего пароля все последующие пароли должны игнорироваться.
# Примечание 1. Приоритет вывода сообщений об ошибке в случае невыполнения нескольких условий:
# LengthError, затем LetterError, а уже после DigitError.
#
#
# Sample Input 1:
#
# arr1
# Arrrrrrrrrrr
# arrrrrrrrrrrrrrr1
# Arrrrrrr1
# Sample Output 1:
#
# LengthError
# DigitError
# LetterError
# Success!
#
# Sample Input 2:
#
# beegeek
# Beegeek123
# Beegeek2022
# Beegeek2023
# Beegeek2024
# Sample Output 2:
# LengthError
# Success!

while True:
    password = input()
    bit_mask = 0

    if len(password) < 9:
        bit_mask = 0b1

    lower_count = 0
    upper_count = 0
    digit_count = 0
    for char in password:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        if char.isdigit():
            digit_count += 1

    if lower_count == 0 or upper_count == 0:
        bit_mask = 1 << 1 | bit_mask

    if digit_count == 0:
        bit_mask = 1 << 2 | bit_mask

    # print result:
    if bit_mask == 0:
        print("Отличный пароль!")
        break
    elif 0b1 & bit_mask:
        print("Слишком короткий пароль")
    elif 0b10 & bit_mask:
        print("Все буквы одного регистра, так не пойдет")
    elif 0b100 & bit_mask:
        print("Пароль без цифр? Переделывай")



