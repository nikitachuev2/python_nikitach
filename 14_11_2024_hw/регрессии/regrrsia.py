
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Загрузка данных из CSV-файлов
feature_data = pd.read_csv('6_x.csv')
target_data = pd.read_csv('6_y.csv')

# Проверка правильности чтения данных
print("Features:\n", feature_data.head())
print("Targets:\n", target_data.head())

# Деление данных на обучающую и тестовую выборки
X_train_set, X_test_set, y_train_set, y_test_set = train_test_split(feature_data, target_data, test_size=0.2, random_state=42)

# Функция для оценки качества модели
def assess_model(model, X_test_set, y_test_set):
    y_predicted = model.predict(X_test_set)  # Генерация предсказанных значений
    mse_value = mean_squared_error(y_test_set, y_predicted)  # Вычисление среднеквадратичной ошибки
    r2_value = r2_score(y_test_set, y_predicted)  # Вычисление коэффициента детерминации
    return mse_value, r2_value

# Линейная регрессия для каждого из признаков
linear_metrics = {}  # Словарь для хранения метрик

for feature in feature_data.columns:
    regression_model = LinearRegression()
    regression_model.fit(X_train_set[[feature]], y_train_set)
    mse_value, r2_value = assess_model(regression_model, X_test_set[[feature]], y_test_set)
    linear_metrics[feature] = [mse_value, r2_value]  # Сохранение метрик модели в словарь

# Множественная регрессия для всех признаков
combined_model = LinearRegression()
combined_model.fit(X_train_set, y_train_set)
mse_value, r2_value = assess_model(combined_model, X_test_set, y_test_set)
linear_metrics['Combined'] = [mse_value, r2_value]  # Сохранение метрик комбинированной модели

print(f"Коэффициенты модели: {combined_model.coef_}")  # Вывод коэффициентов множественной регрессии
print(f"Свободный член (intercept): {combined_model.intercept_}")  # Вывод свободного члена

# Построение полиномиальной регрессии
for feature in feature_data.columns:
    # Полиномиальная регрессия 2-й степени
    polynomial_features = PolynomialFeatures(degree=2)
    X_poly_train_set = polynomial_features.fit_transform(X_train_set[[feature]])
    X_poly_test_set = polynomial_features.transform(X_test_set[[feature]])  # Преобразование выборок

    polynomial_model = LinearRegression()
    polynomial_model.fit(X_poly_train_set, y_train_set)
    mse_value, r2_value = assess_model(polynomial_model, X_poly_test_set, y_test_set)
    linear_metrics[feature + '^2'] = [mse_value, r2_value]  # Сохранение метрик полиномиальной модели 2-й степени

# Полиномиальная регрессия 3-й степени
for feature in feature_data.columns:
    polynomial_features = PolynomialFeatures(degree=3)
    X_poly_train_set = polynomial_features.fit_transform(X_train_set[[feature]])
    X_poly_test_set = polynomial_features.transform(X_test_set[[feature]])  # Преобразование выборок

    polynomial_model = LinearRegression()
    polynomial_model.fit(X_poly_train_set, y_train_set)
    mse_value, r2_value = assess_model(polynomial_model, X_poly_test_set, y_test_set)
    linear_metrics[feature + '^3'] = [mse_value, r2_value]  # Сохранение метрик полиномиальной модели 3-й степени

# Создание сводной таблицы результатов
results_table = pd.DataFrame(linear_metrics).T  # Преобразование словаря метрик в DataFrame и транспонирование

results_table.columns = ['MSE', 'R^2']  # Название столбцов
print(results_table)  # Вывод сводной таблицы

# На основании анализа данных решено построить полиномиальную регрессию 2-й степени с x2 и x3
# Проверяем наличие столбца 'X1' перед его удалением
if 'X1' in X_test_set.columns:
    X_test_set = X_test_set.drop(columns='X1')  # Удаляем столбец X1 из тестовой выборки
if 'X1' in X_train_set.columns:
    X_train_set = X_train_set.drop(columns='X1')  # Удаляем столбец X1 из обучающей выборки

polynomial_features = PolynomialFeatures(degree=2)
X_poly_train_set = polynomial_features.fit_transform(X_train_set)  # Преобразование обучающей выборки
X_poly_test_set = polynomial_features.transform(X_test_set)  # Преобразование тестовой выборки

polynomial_model = LinearRegression()
polynomial_model.fit(X_poly_train_set, y_train_set)
mse_value, r2_value = assess_model(polynomial_model, X_poly_test_set, y_test_set)
linear_metrics['Combined^2'] = [mse_value, r2_value]  # Сохранение метрик полиномиальной модели 2-й степени

results_table = pd.DataFrame(linear_metrics).T  # Преобразование словаря метрик в DataFrame и транспонирование
results_table.columns = ['MSE', 'R^2']  # Название столбцов
print(results_table)  # Вывод сводной таблицы
