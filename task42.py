# DONE


#todo:
# Создайте функцию-генератор, которая создает последовательность числовых
# палиндромов: 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212 …

def gen_palindrome(upper_value):
    palindrome = [i for i in range(1, upper_value+1) if str(i) == str(i)[::-1]]
    return palindrome

print(gen_palindrome(1000))