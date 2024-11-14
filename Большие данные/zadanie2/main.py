
import zipfile
import os
import dask.dataframe as dd
from sqlalchemy import create_engine

# Функция для разархивации ZIP файла
def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Файл {zip_path} был успешно разархивирован в {extract_to}")

# Путь к ZIP файлу
zip_file_path = 'recipes_full.zip'
# Папка, куда будет разархивирован файл
extract_directory = os.path.dirname(os.path.abspath(zip_file_path))

# Создаем папку, если она не существует
os.makedirs(extract_directory, exist_ok=True)

# Разархивируем файл
unzip_file(zip_file_path, extract_directory)

# Путь к загруженному CSV файлу, включая подпапку
csv_directory = os.path.join(extract_directory, 'recipes_full')

# Читаем все CSV файлы из директории в Dask DataFrame с указанием типов данных
df = dd.read_csv(os.path.join(csv_directory, '*.csv'), dtype={'minutes': 'float64', 'n_steps': 'float64'})

# Выводим метаинформацию о Dask DataFrame
print(f"Число партий: {df.npartitions}")
print("Типы столбцов:\n", df.dtypes)

# Выводим первые 5 и последние 5 строк таблицы
print("Первые 5 строк:\n", df.head())
print("Последние 5 строк:\n", df.tail())

# Подсчёт строк в каждом блоке
for i in range(df.npartitions):
    print(f"Количество строк в блоке {i}: {df.get_partition(i).shape[0].compute()}")

# Находим максимум в столбце n_steps
max_n_steps = df['n_steps'].max()
print("Максимальное значение в n_steps:", max_n_steps.compute())

# Подсчёт количества отзывов с группировкой по месяцам добавления
reviews_per_month = df.groupby(df['submitted'].dt.to_period('M')).size().compute()
print("Количество отзывов по месяцам:\n", reviews_per_month)

# Находим пользователя, отправлявшего рецепты чаще всех
top_user = df['contributor_id'].value_counts().idxmax().compute()
print(f"Пользователь, отправлявший рецепты чаще всех: {top_user}")

# Находим самый первый и самый последний по дате отправления рецепт
first_recipe = df.loc[df['submitted'].idxmin()].compute()  # idxmin() будет работать только с стандартным DataFrame
last_recipe = df.loc[df['submitted'].idxmax()].compute()
print(f"Самый первый рецепт:\n{first_recipe}\n")
print(f"Самый последний рецепт:\n{last_recipe}\n")

# Создаем соединение с базой данных SQLite
engine = create_engine('sqlite:///recipes.db')

# Загружаем рецепты в базу данных SQLite
df.to_sql('recipes', engine, if_exists='replace', index=False)

# Отбор рецептов с временем приготовления меньше медианы и количеством шагов меньше среднего
median_time = df['minutes'].median().compute()  # Вычисляем медиану времени приготовления
mean_steps = df['n_steps'].mean().compute()      # Вычисляем среднее количество шагов

# Фильтруем DataFrame
filtered_recipes = df[(df['minutes'] < median_time) & (df['n_steps'] < mean_steps)]

# Сохраняем отобранные рецепты в файл .csv
filtered_recipes.to_csv('filtered_recipes.csv', single_file=True, index=False)  # Сохраняем в один файл

print(f"Отобранное количество рецептов: {len(filtered_recipes)}")