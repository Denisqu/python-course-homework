#todo: Напишите программу, которая:
# Получает на вход две строки, в которых перечисляются книги, прочитанные двумя учениками.
# Выводит количество книг, которые прочитали оба ученика.
# Пример ввода:
# Война и мир, Над пропастью во ржи, Мастер и Маргарита, Идиот
# Евгений Онегин, Идиот, Мастер и Маргарита, Война и мир

inputs = []
for i in range(0,2):
    inputs.append(input("Введите книги ученика в формате: 'Название книги1, Название книги2, ...'\n"))

splited_inputs = []
for i, input in enumerate(inputs):
    splited_inputs.append(input.split(","))
    for j, title in enumerate(splited_inputs[i]):
        splited_inputs[i][j] = title.strip()
    splited_inputs[i] = set(splited_inputs[i])

print(f"Книги, прочитанные двумя учениками: {splited_inputs[0].intersection(splited_inputs[1])}")