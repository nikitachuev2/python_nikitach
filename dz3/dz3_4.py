
def file_statistics(file_path):
    """
    Эта функция принимает путь к текстовому файлу и возвращает статистику о нем в виде словаря.
    В словаре содержатся следующие ключи:
    - 'Количество строк в файле: '
    - 'Количество слов: '
    - 'Количество символов: '
    - 'Самое длинное слово: '
    - 'Количество символов в самом длинном слове: '
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()  # Читаем весь текст из файла

        lines_count = file_content.count('\n') + (1 if file_content else 0)  # Подсчитываем количество строк
        words_list = file_content.split()  # Разбиваем текст на отдельные слова
        words_count = len(words_list)  # Подсчитываем общее количество слов
        chars_count = len(file_content)  # Подсчитываем общее количество символов

        longest_word = max(words_list, key=len) if words_list else ''  # Находим слово с максимальной длиной
        longest_word_length = len(longest_word)  # Определяем длину самого длинного слова

        return {
            'Количество строк в файле: ': lines_count,
            'Количество слов: ': words_count,
            'Количество символов: ': chars_count,
            'Самое длинное слово: ': longest_word,
            'Количество символов в самом длинном слове: ': longest_word_length
        }
    except FileNotFoundError:
        print(f"Файл по пути {file_path} не найден.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")
        return None

# Запрашиваем у пользователя путь к текстовому файлу с указанием кодировки
user_file_path = input('Введите путь к текстовому файлу (файл должен быть в кодировке UTF-8): ')
file_stats = file_statistics(user_file_path)  # Получаем статистику о файле

# Выводим результаты на экран с пояснением
if file_stats:
    print("Статистика файла:")
    for key, value in file_stats.items():
        print(f"{key} {value}")

