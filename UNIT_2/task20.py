# todo: Ввод: 2 слова, разделенных пробелами. Для ввода используем функцию s = input().split()
#  Определить, являются ли эти слова анаграммами (словами с одинаковым набором букв). Если да, то True. Если нет, то False.
#  (Примеры: АКВАРЕЛИСТ-КАВАЛЕРИСТ, АНТИМОНИЯ-АНТИНОМИЯ, АНАКОНДА-КАНОНАДА, ВЕРНОСТЬ-РЕВНОСТЬ, ВЛАДЕНИЕ-ДАВЛЕНИЕ, ЛЕПЕСТОК-ТЕЛЕСКОП)

input_str_list = input().split()
# Create list of maps { "char":count }:
list_dicts_char_to_count = []
for word in input_str_list:
    word_map = {}
    for char in word:
        get_count = word_map.get(char, None)
        if get_count is not None:
            word_map[char] += 1
        else:
            word_map[char] = 1
    list_dicts_char_to_count.append(word_map)

# Compare maps:
isAnagram = True
for char, count in list_dicts_char_to_count[0].items():
    if list_dicts_char_to_count[1].get(char, None) is None\
            or list_dicts_char_to_count[1][char] != count:
        isAnagram = False
        break

print(f"Is anagram = {isAnagram}")