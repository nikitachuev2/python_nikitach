
def merge_files(file_paths, write_to_file=True):
    """
    Функция merge_files принимает список file_paths, содержащий пути к текстовым файлам.
    Она объединяет содержимое всех указанных файлов в одну строку и возвращает ее.
    Если параметр write_to_file равен True (по умолчанию), то содержимое также записывается в файл "merged_file.txt".
    """
    merged_content = ""  # Переменная, в которой будет храниться объединенное содержимое файлов

    # Проходим по всем указанным путям к файлам
    for file_path in file_paths:
        try:
            # Открываем файл в режиме чтения с кодировкой UTF-8
            with open(file_path, 'r', encoding='utf-8') as file:
                merged_content += file.read()  # Добавляем содержимое файла к merged_content
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
            continue  # Пропускаем файл, если он не найден
        except Exception as e:
            print(f"Произошла ошибка при чтении файла {file_path}: {e}")
            continue  # Пропускаем файл при возникновении других ошибок

    # Если нужно записать объединенное содержимое в файл
    if write_to_file:
        # Открываем файл "merged_file.txt" в режиме записи с кодировкой UTF-8
        with open('merged_file.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(merged_content)  # Записываем объединенное содержимое в файл

    return merged_content  # Возвращаем объединенное содержимое файлов

# Запрашиваем у пользователя количество файлов для объединения
num_files = int(input('Сколько файлов хотите объединить? '))

# Создаем список для хранения путей к файлам
file_paths = []

# Просим пользователя ввести пути к файлам
for i in range(num_files):
    file_path = input(f'Введите {i + 1}-ый путь к файлу: ')
    file_paths.append(file_path)  # Добавляем путь к файлу в список

# Спрашиваем, нужно ли записывать объединенное содержимое в файл
write_to_file_input = input('Записывать ли содержимое в новый файл merged_file.txt? (0 - нет, 1 - да) ')
write_to_file = write_to_file_input == '1'  # Преобразуем ввод в булевый тип (True/False)

# Вызываем функцию merge_files с указанными параметрами
merged_content = merge_files(file_paths, write_to_file=write_to_file)

# Выводим объединенное содержимое файлов
print("Объединенное содержимое файлов:")
print(merged_content)

# Обратите внимание, что все файлы должны быть в кодировке UTF-8 для корректного чтения и записи.

