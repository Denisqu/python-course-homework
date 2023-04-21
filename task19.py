#todo: Напишите калькулятор (простой). На вход подается строка, например:
# 1 + 2  или  5 – 3  или  3 * 4  или  10 / 2.
# Вывод: сосчитать и напечатать результат операции.
# Гарантируется, что два операнда и операция есть в каждой строчке, и все они разделены пробелами.


str_operand_to_operation = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

expression_str = input("Input an arithmetic expression: \n")
expression_splitted_str_list = expression_str.split(" ")

operand = expression_splitted_str_list[1]
x = int(expression_splitted_str_list[0])
y = int(expression_splitted_str_list[2])

result = str_operand_to_operation[operand](x, y)

print(f"Operation result = {result}")
