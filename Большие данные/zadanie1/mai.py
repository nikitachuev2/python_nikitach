
import zipfile
import sqlite3
import os
import pandas as pd
from sqlalchemy import create_engine

def unzip_file(zip_path, extract_to):
    """
    Функция для разархивации ZIP файла в указанную директорию.
    
    :param zip_path: Путь к ZIP файлу.
    :param extract_to: Папка, куда будет разархивирован файл.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)  # Разархивируем все содержимое в указанную папку.
    print(f"Файл {zip_path} был успешно разархивирован в {extract_to}")
  
# Путь к ZIP файлу
zip_file_path = 'recipes_full.zip'
# Папка, куда будет разархивирован файл
extract_directory = os.path.dirname(os.path.abspath(zip_file_path))
# Создаем папку, если она не существует
os.makedirs(extract_directory, exist_ok=True) 

# Разархивируем файл
unzip_file(zip_file_path, extract_directory)

# Запрос имени CSV файла у пользователя, с подсказкой по умолчанию
default_csv_filename = 'recipes_full_0.csv'
user_input = input(f"Введите название CSV файла (по умолчанию '{default_csv_filename}'): ")

# Если пользователь ничего не ввел, используем имя по умолчанию
csv_file_name = user_input if user_input else default_csv_filename

# Путь к загруженному CSV файлу, включая подпапку
csv_directory = os.path.join(extract_directory, 'recipes_full')  # Путь до подпапки с рецептами
first_file_path = os.path.join(csv_directory, csv_file_name)  # Полный путь к CSV файлу

try:
    # Читаем CSV файл
    df = pd.read_csv(first_file_path)
except FileNotFoundError:
    print(f"Ошибка: Файл '{csv_file_name}' не найден. Убедитесь, что он существует в директории '{csv_directory}'.")
    exit()  # Выходим из программы при ошибке

# Проверяем типы данных столбцов в DataFrame
print("Типы данных столбцов:\n", df.dtypes)

# Находим максимальное значение в столбце n_steps
max_n_steps = df['n_steps'].max()
print(f"Максимальное количество шагов: {max_n_steps}")

# Преобразуем дату подачи в формат даты
df['date'] = pd.to_datetime(df['submitted'])

# Получаем количество отзывов по месяцам
reviews_per_month = df.groupby(df['date'].dt.to_period('M')).size()
print("Количество отзывов по месяцам:\n", reviews_per_month)

# Находим пользователя, который отправлял рецепты чаще всех
top_user = df['contributor_id'].value_counts().idxmax()
print(f"Пользователь, отправлявший рецепты чаще всех: {top_user}")

# Находим самый первый и самый последний рецепт в DataFrame
first_recipe = df.loc[df['date'].idxmin()]
last_recipe = df.loc[df['date'].idxmax()]

print(f"Самый первый рецепт:\n{first_recipe}\n")
print(f"Самый последний рецепт:\n{last_recipe}\n")

# Определяем медианы по количеству ингредиентов и времени приготовления
medians = df[['n_ingredients', 'minutes']].median()
print(f"Медианы по количеству ингредиентов и времени приготовления:\n{medians}\n")

# Находим самый простой рецепт (по количеству ингредиентов, времени и шагов)
simplest_recipe = df.sort_values(by=['n_ingredients', 'minutes', 'n_steps'], ascending=[True, True, True]).iloc[0]
print("Самый простой рецепт:")
print(simplest_recipe)

# Загружаем рецепты в базу данных SQLite
conn = sqlite3.connect('recipes.db')  # Создаем или открываем базу данных SQLite
df.to_sql('recipes', conn, if_exists='replace', index=False)  # Заменяем таблицу, если она существует

# Проверяем загружены ли данные из таблицы
loaded_df = pd.read_sql('SELECT * FROM recipes', conn)
print("Данные, загруженные из базы данных:\n", loaded_df)

conn.close()  # Закрываем соединение с базой данных

# Создаем подключение к базе данных SQLite с помощью SQLAlchemy

engine = create_engine('sqlite:///recipes.db')  # Используем созданную базу данных для подключения

# 1. Загружаем DataFrame в базу данных SQLite (уже сделано выше, если нужно можно убрать)
# df.to_sql('recipes', engine, if_exists='replace', index=False)  # Заменяем таблицу, если она существует

# 2. Отбор рецептов с временем приготовления меньше медианы и количеством шагов меньше среднего
median_time = df['minutes'].median()  # Вычисляем медиану времени приготовления
mean_steps = df['n_steps'].mean()      # Вычисляем среднее количество шагов

# Фильтруем DataFrame по условиям
filtered_recipes = df[(df['minutes'] < median_time) & (df['n_steps'] < mean_steps)]

# 3. Сохранение отобранного DataFrame в файл .csv
filtered_recipes.to_csv('filtered_recipes.csv', index=False)  # Сохраняем отобранные рецепты в CSV файл

print(f"Отобранное количество рецептов: {len(filtered_recipes)}")  # Выводим количество отобранных рецептов
