#todo: Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв: G → C, C → G, T → A, A→T.
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК. Например:
#В вод: GGCTAA
# Вывод: CCGATT

def dnk_to_rnk(dnk_string):
    def get_rnk_char(dnk_char):
        match dnk_char:
            case "G":
                return "C"
            case "C":
                return "G"
            case "T":
                return "A"
            case "A":
                return "T"
            case _:
                return "_"
    rnk = ""
    for char in dnk_string:
        rnk += get_rnk_char(char)
    return rnk

dnk = "GGCTAA"
print(dnk_to_rnk(dnk))
