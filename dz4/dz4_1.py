
import re

def find_emails_and_phones(input_file, output_file):
    # Открываем входной файл, указанный пользователем
    with open(input_file, "r") as file:
        text = file.read()

    # Находим все email-адреса в тексте с помощью регулярного выражения
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

    # Находим все номера телефонов в тексте с помощью регулярного выражения
    phones = re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text)

    # Открываем выходной файл, указанный пользователем, для записи
    with open(output_file, "w") as file:
        # Записываем найденные email-адреса в выходной файл
        file.write("Email-адреса:\n")
        for email in emails:
            file.write(email + "\n")

        # Записываем найденные номера телефонов в выходной файл
        file.write("\nНомера телефонов:\n")
        for phone in phones:
            file.write(phone + "\n")

    # Выводим информацию о результатах поиска в консоль
    print(f"Найдено email-адресов: {len(emails)}")
    print(f"Найдено номеров телефонов: {len(phones)}")
    print(f"Результаты сохранены в файле '{output_file}'.")

# Запрашиваем у пользователя имена входного и выходного файлов
print("Введите имя входного файла, в котором нужно искать email-адреса и номера телефонов:")
input_file = input()
print("Введите имя выходного файла, в который нужно сохранить результаты:")
output_file = input()

# Вызываем функцию, передавая пользовательские имена файлов
find_emails_and_phones(input_file, output_file)
