
# Получение входного списка от пользователя
num_persons = int(input("Введите количество человек: "))
persons = []
for i in range(num_persons):
    name = input(f"Введите имя {i+1}-го человека: ")
    age = int(input(f"Введите возраст {i+1}-го человека: "))
    persons.append((name, age))

#В этом блоке кода мы запрашиваем у пользователя количество человек, а затем в цикле for просим ввести имя и возраст каждого человека. Мы сразу создаем список persons, состоящий из кортежей (name, age).

# Фильтрация и сортировка списка
filtered_persons = [(name, age) for name, age in persons if age > 18]
filtered_persons.sort(key=lambda x: x[1])

#В этом блоке мы используем списочное выражение (list comprehension) для фильтрации списка persons. Мы создаем новый список filtered_persons, в который включаем только те кортежи, у которых возраст (age) больше 18 лет.

#Далее, мы сортируем список filtered_persons по возрасту (x[1]) с помощью метода sort(). Для этого мы используем key=lambda x: x[1], чтобы задать критерий сортировки.

# Вывод результата
print(filtered_persons)
