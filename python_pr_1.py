
# Создаем список слов
words = ['tree', 'mountain', 'river', 'cloud', 'book', 
         'chair', 'light', 'window', 'phone', 'mirror', 
         'sky', 'dream', 'road', 'smile', 'shadow']

# Функция для вычисления веса слова
def calculate_weight(word):
    weight = 0  # Инициализируем вес слова как 0
    # Проходим по каждому символу в слове
    for char in word:
        weight += ord(char)  # Вычисляем значение Unicode символа и добавляем его к весу
    return weight  # Возвращаем общий вес слова


# Создаем словарь с весами слов, где ключ — вес, а значение — слово
weights_dict = {calculate_weight(word): word for word in words}

# Сортируем словарь по весам, чтобы получить список кортежей (вес, слово)
sorted_weights = sorted(weights_dict.items())  # Сортируем по ключам (весам)

# Выводим отсортированный список на экран
print("Отсортированный список слов по весам (вес: слово):")
for weight, word in sorted_weights:
    print(f"{weight}: {word}")

# Функция для бинарного поиска в отсортированном списке
def binary_search(weighted_list, target):
    low = 0  # Устанавливаем начальный индекс
    high = len(weighted_list) - 1  # Устанавливаем конечный индекс

    while low <= high:  # Пока не выйдем за границы списка
        mid = (low + high) // 2  # Находим средний индекс
        mid_weight = weighted_list[mid][0]  # Получаем вес из отсортированного списка

        if mid_weight == target:  # Если нашли нужный вес
            return mid  # Возвращаем индекс
        elif mid_weight < target:  # Если вес меньше, ищем в правой части
            low = mid + 1
        else:  # Если вес больше, ищем в левой части
            high = mid - 1

    return -1  # Если не найдено, возвращаем -1

# Запрашиваем у пользователя слово для поиска
input_word = input("Введите слово для поиска: ")

# Вычисляем вес введенного слова
input_weight = calculate_weight(input_word)

# Выполняем бинарный поиск по весам
index = binary_search(sorted_weights, input_weight)

# Проверяем результат поиска и выводим информацию
if index != -1:
    found_weight, found_word = sorted_weights[index]  # Получаем вес и слово из найденного индекса
    print(f"Слово: '{found_word}', Вес: {found_weight}, Индекс в отсортированном списке: {index}")
else:
    print("Слово не найдено.")
