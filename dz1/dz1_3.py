
# Создаем пустой список для хранения чисел
numbers = []

# Запрашиваем ввод чисел от пользователя
while True:
    num = int(input("Введите число (-1 для остановки): "))
    if num == -1:
        break
    numbers.append(num)

# Выводим длину списка
print("Длина списка:", len(numbers))

# Выводим сумму элементов в списке через цикл
total_sum = 0
for number in numbers:
    total_sum += number
print("Сумма элементов (через цикл):", total_sum)

# Выводим сумму элементов в списке через метод списка
print("Сумма элементов (через метод списка):", sum(numbers))

# Выводим только четные элементы списка
print("Четные элементы списка:")
for number in numbers:
    if number % 2 == 0:
        print(number)

