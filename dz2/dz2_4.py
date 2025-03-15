
# Получение входного словаря от пользователя
input_dict = {}
num_items = int(input("Введите количество элементов в словаре: "))
for _ in range(num_items):
    key = input(f"Введите ключ {len(input_dict) + 1}: ")
    value = input(f"Введите значение для ключа {key}: ")
        input_dict[key] = value

# Создание нового словаря с перевернутыми ключами и значениями
output_dict = {}
for key, value in input_dict.items():
    output_dict[value] = key

# Вывод результата
print("Исходный словарь:", input_dict)
print("Результирующий словарь:", output_dict)
