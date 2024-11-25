
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import GridSearchCV

# 1. Загрузка датасета о раке молочной железы
# Мы используем встроенный датасет из библиотеки sklearn.
data = load_breast_cancer()

# Преобразуем данные в DataFrame для удобства работы
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target  # Добавляем целевую переменную

# 2. Исследуем данные
print("Первые 5 строк датасета:")
print(df.head())  # Выводим первые 5 строк

print("\nОбщая информация о датасете:")
print(df.info())  # Выводим информацию о датасете

print("\nСтатистическое описание числовых признаков:")
print(df.describe())  # Выводим описательную статистику

# Проверяем на наличие пропусков
print("\nПроверка на наличие пропусков:")
print(df.isnull().sum())  # Проверяем на наличие пропусков по каждому столбцу

# В данном датасете нет пропусков, но если бы они были, мы могли бы использовать:
# df.fillna(method='ffill', inplace=True)  # Пример заполнения пропусков

# 3. Обработка и стандартизация данных
# Разделяем предикторы (функции) и целевую переменную
X = df.drop('target', axis=1)  # Убираем целевую переменную из датасета
y = df['target']  # Сохраняем целевую переменную

# Стандартизация данных
scaler = StandardScaler()  # Выбираем метод стандартизации
X_scaled = scaler.fit_transform(X)  # Применяем стандартизацию

# 4. Разделение данных на обучающую и тестовую выборки
# 80% данных будет использоваться для обучения, 20% - для тестирования
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

# 5. Обучение различных моделей классификации

# 5.1 Логистическая регрессия
log_reg = LogisticRegression(max_iter=10000)  # Увеличим количество итераций для сходимости
log_reg.fit(X_train, y_train)  # Обучаем модель
y_pred_log_reg = log_reg.predict(X_test)  # Предсказание на тестовой выборке

# 5.2 SVM (машина наименьших квадратов)
svm_model = SVC()  # Создание модели SVM
svm_model.fit(X_train, y_train)  # Обучаем модель
y_pred_svm = svm_model.predict(X_test)  # Предсказание на тестовой выборке

# 5.3 KNN (к-ближайших соседей)
knn_model = KNeighborsClassifier(n_neighbors=5)  # Создание модели KNN
knn_model.fit(X_train, y_train)  # Обучаем модель
y_pred_knn = knn_model.predict(X_test)  # Предсказание на тестовой выборке

# 5.4 Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)  # Создание модели Random Forest
rf_model.fit(X_train, y_train)  # Обучаем модель
y_pred_rf = rf_model.predict(X_test)  # Предсказание на тестовой выборке

# 6. Оценка моделей
models = ['Logistic Regression', 'SVM', 'KNN', 'Random Forest']
predictions = [y_pred_log_reg, y_pred_svm, y_pred_knn, y_pred_rf]

for model_name, preds in zip(models, predictions):
    print(f"\n{model_name}:\n")
    print("Точность:", accuracy_score(y_test, preds))  # Точность
    print("Отчет по классификации:\n", classification_report(y_test, preds))  # Отчет по классификации

    print("Матрица ошибок:\n", confusion_matrix(y_test, preds))  # Матрица ошибок

# 7. Настройка гиперпараметров для Random Forest
# Определяем параметры для GridSearch
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_features': ['auto', 'sqrt'],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid,
                           cv=3, n_jobs=-1, verbose=2)

# Тренируем модель с помощью GridSearch
grid_search.fit(X_train, y_train)

# Лучшая модель после подбора
print("\nЛучшие параметры для Random Forest:")
print(grid_search.best_params_)  # Выводим лучшие параметры
best_rf_model = grid_search.best_estimator_  # Лучшая модель
best_rf_predictions = best_rf_model.predict(X_test)  # Предсказания на тестах

# Оценка лучшей модели
print("Точность лучшей модели Random Forest с подобранными параметрами:", accuracy_score(y_test, best_rf_predictions))
print("Отчет по классификации для лучшей модели:\n", classification_report(y_test, best_rf_predictions))
print("Матрица ошибок для лучшей модели:\n", confusion_matrix(y_test, best_rf_predictions))
