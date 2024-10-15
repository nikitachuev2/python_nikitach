
import string # Импортируем модуль string, который содержит константы с различными символами
import random # Импортируем модуль random для генерации случайных чисел

# Функция для генерации пароля
def generate_password(length):
    # Объединяем все символы, которые можно использовать в пароле
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Генерируем случайный пароль, состоящий из выбранных символов
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Основная часть программы
password_length = int(input("Enter the desired password length: "))
generated_password = generate_password(password_length)

print("Generated password:", generated_password)
