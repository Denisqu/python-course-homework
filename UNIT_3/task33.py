# todo:
#     Напишите программу, которая определяет и печатает «похожие» слова. Слово называется похожим на другое слово,
#     если его гласные буквы находятся там же, где находятся гласные буквы другого слова, например:
#     дорога и пароход - похожие слова (гласные буквы на втором, четвертом и шестом местах),
#     станок и прыжок - похожие слова, питон и удав непохожие слова.
#     Считаем, что в русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е).
#     Ввод: x –первое слово, например, питон. n – количество слов для сравнения, например 6.
#     Дальше вводятся 6 слов, например: поросенок, титан, итог, лавка, погост, кино.
#     Вывод - слова, похожие на питон: титан, погост, кино

test_word_to_compare = "питон"
test_word_count = 6
test_input = "поросенок, титан, итог, лавка, погост, кино"

def parse_raw_input_to_str_list(raw_string):
    parsed_list = raw_string.split(",")
    parsed_list = [i.strip() for i in parsed_list]
    return parsed_list

def find_similar_word(word_to_compare, words_list):
    def get_vowel_indexes(word):
        ru_vowel_letters = {"а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"}
        vowel_indexes = []
        for i, char in enumerate(word):
            if char in ru_vowel_letters: vowel_indexes.append(i)

        return vowel_indexes

    def are_words_similar(word1_vowel_indexes, word2_vowel_indexes):
        return set(word1_vowel_indexes) == set(word2_vowel_indexes)

    similar_words = []
    word_to_compare_vowel_indexes = get_vowel_indexes(word_to_compare)
    for word in words_list:
        if are_words_similar(word_to_compare_vowel_indexes,
                             get_vowel_indexes(word)):
            similar_words.append(word)

    return similar_words


print(find_similar_word(test_word_to_compare,
                        parse_raw_input_to_str_list(test_input)))
