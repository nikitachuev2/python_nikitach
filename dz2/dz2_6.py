# ВВод строки
s = input('ведите строку')
# Приведение всех слов к нижнему регистру
s_lower = s.lower()

# Очистка строки от знаков препинания
s_clean = ''.join(char for char in s_lower if char.isalnum() or char.isspace())

# Создание списка слов
words_list = s_clean.split()

# Создание словаря с частотой встречаемости слов
word_freq = {}
for word in words_list:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Сортировка словаря по убыванию частоты встречаемости слов
sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))

# Вывод результата
print("Приведение к нижнему регистру:", s_lower)
print("Очистка от знаков препинания:", s_clean)
print("Список слов:", words_list)
print("Словарь с частотой встречаемости слов:", sorted_word_freq)
