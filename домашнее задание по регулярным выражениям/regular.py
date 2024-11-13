
import re

def open_file(file_path):
    """Открывает текстовый файл и возвращает его содержимое."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()  # Читаем содержимое файла
    except Exception as e:
        print(f"Ошибка при открытии файла: {e}")  # Выводим ошибку при открытии файла
        return None  # Возвращаем None при ошибке

def find_sentences(text):
    """Ищет все предложения, заканчивающиеся на точку, восклицательный или вопросительный знак."""
    pattern = r'[^.!?]*[.!?]'  # Регулярное выражение для нахождения предложений
    return re.findall(pattern, text)  # Возвращаем найденные предложения

def find_proper_nouns(text):
    """Ищет имена собственные (начинаются с заглавной буквы)."""
    pattern = r'\b[A-ZА-ЯЁ][a-zа-яё]+\b(?:\s+[A-ZА-ЯЁ][a-zа-яё]+)*'  # Регулярное выражение для имен
    return re.findall(pattern, text)  # Возвращаем найденные имена собственные

def find_quotes(text):
    """Ищет цитаты, заключенные в одиночные или двойные кавычки."""
    pattern = r"['\"]([^'\"]+)['\"]"  # Регулярное выражение для нахождения цитат в разных кавычках
    return re.findall(pattern, text)  # Возвращаем найденные цитаты

# Пример использования
if __name__ == "__main__":  # Обратите внимание, здесь должно быть __name__, а не name.
    file_path = 'example_tekst.txt'  # Путь к файлу с текстом
    content = open_file(file_path)  # Получаем содержимое файла

    if content:  # Если файл успешно открыт и прочитан
        # Обработка каждого регулярного выражения
        patterns = {
            "Предложения": find_sentences(content),  # Находим все предложения
            "Имена собственные": find_proper_nouns(content),  # Находим имена собственные
            "Цитаты": find_quotes(content),  # Находим все цитаты
        }

        # Вывод результатов
        for description, matches in patterns.items():
            count = len(matches)  # Подсчитываем количество найденных совпадений
            print(f"Поиск '{description}':")  # Информируем о типе поиска
            print(f"Всего найдено: {count}")  # Выводим общее количество найденных совпадений
            print("Первые 10 coincidences:")
            print(matches[:10] if matches else "Нет совпадений.")  # Выводим первые 10 совпадений
            print()  # Пустая строка для разделения выводов
