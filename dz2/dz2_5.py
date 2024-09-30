
# Получение списка множеств от пользователя
num_sets = int(input("Введите количество множеств: "))
sets_list = []
for i in range(num_sets):
    set_elements = input(f"Введите элементы {i+1}-го множества через пробел: ").split()
    sets_list.append(set(map(int, set_elements)))

# Вычисление пересечения множеств
intersection = sets_list[0]
for i in range(1, len(sets_list)):
    intersection = intersection.intersection(sets_list[i])

# Вывод результата
print("Пересечение множеств:", intersection)
