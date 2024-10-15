
import numpy as np

# Шаг 1: Сгенерируем случайную квадратную матрицу размером 10 на 10
print("Шаг 1: Генерация случайной квадратной матрицы 10x10")
matrix = np.random.rand(10, 10)
print(matrix)
print()

# Шаг 2: Найдем определитель матрицы
print("Шаг 2: Вычисление определителя матрицы")
det = np.linalg.det(matrix)
print(f"Определитель матрицы: {det:.2f}")

# Обработаем вариант с вырожденной матрицей (определитель равен нулю)
if abs(det) < 1e-10:
    print("Матрица является вырожденной (определитель равен нулю)")
else:
    print("Матрица не является вырожденной")
print()

# Шаг 3: Транспонируем матрицу
print("Шаг 3: Транспонирование матрицы")
transposed_matrix = matrix.T
print(transposed_matrix)
print()

# Шаг 4: Найдем ранг матрицы
print("Шаг 4: Вычисление ранга матрицы")
rank = np.linalg.matrix_rank(matrix)
print(f"Ранг матрицы: {rank}")
print()

# Шаг 5: Найдем собственные значения и собственные вектора матрицы
print("Шаг 5: Вычисление собственных значений и собственных векторов матрицы")
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Собственные значения:")
print(eigenvalues)
print("Собственные вектора:")
print(eigenvectors)
print()

# Шаг 6: Сгенерируем вторую матрицу размером 10 на 10 и выполним сложение и умножение
print("Шаг 6: Сложение и умножение двух матриц")
matrix2 = np.random.rand(10, 10)
print("Матрица 1:")
print(matrix)
print("Матрица 2:")
print(matrix2)

addition = matrix + matrix2
print("Сложение матриц:")
print(addition)

multiplication = np.matmul(matrix, matrix2)
print("Умножение матриц:")
print(multiplication)
