
import zipfile
import os
import dask.dataframe as dd
import matplotlib
matplotlib.use('Agg')  # Используем бэкенд Agg для работы без графического интерфейса
import matplotlib.pyplot as plt

# Функция для извлечения содержимого ZIP файла
def extract_zip(zip_filepath, output_directory):
    with zipfile.ZipFile(zip_filepath, 'r') as zip_file:
        zip_file.extractall(output_directory)
    print(f"Файл {zip_filepath} успешно извлечен в {output_directory}")

# Путь к ZIP файлу
zip_file_location = 'recipes_full.zip'
# Определяем директорию для извлечения архива
output_dir = os.path.dirname(os.path.abspath(zip_file_location))
# Извлекаем файл
extract_zip(zip_file_location, output_dir)

# Путь к распакованным данным
csv_folder = os.path.join(output_dir, 'recipes_full')

# Загружаем все CSV файлы в Dask DataFrame с указанием типов данных
dataframe = dd.read_csv(os.path.join(csv_folder, '*.csv'), dtype={'minutes': 'float64', 'n_steps': 'float64', 'submitted': 'str'})

# Выводим информацию о Dask DataFrame
print(f"Количество партиций: {dataframe.npartitions}")
print("Типы столбцов:\n", dataframe.dtypes)

# Выводим первые 5 и последние 5 записей таблицы
print("Первые 5 записей:\n", dataframe.head())
print("Последние 5 записей:\n", dataframe.tail())

# Подсчет строк в каждой партиции
for index in range(dataframe.npartitions):
    print(f"Количество строк в партиции {index}: {dataframe.get_partition(index).shape[0].compute()}")

# Находим максимальное значение в столбце n_steps
max_steps = dataframe['n_steps'].max()
print("Максимальное значение в n_steps:", max_steps.compute())

# Визуализируем график максимального количества шагов
plt.figure(figsize=(8, 6))
plt.bar(['Максимальные n_steps'], [max_steps.compute()], color='blue')
plt.title('Максимальное количество шагов (n_steps)')
plt.ylabel('Количество шагов')
plt.savefig('dask_max_steps_count.png')
plt.close()  # Закрываем фигуру

# Подсчет количества отзывов с группировкой по месяцам добавления
dataframe['submission_time'] = dd.to_datetime(dataframe['submitted'])  # Преобразуем дату подачи в формат даты
monthly_reviews = dataframe.groupby(dataframe['submission_time'].dt.to_period('M')).size().compute()
print(monthly_reviews)  # Выводим количество по месяцам

# Находим пользователя, который отправлял рецепты чаще других
most_active_user = dataframe['contributor_id'].value_counts().idxmax().compute()
print(f"Пользователь, отправлявший рецепты чаще всех: {most_active_user}")

# Первый и последний рецепт
latest_recipe = dataframe.nlargest(1, 'submission_time').compute()
print(f'Последний по дате рецепт: \n{latest_recipe}')
earliest_recipe = dataframe.loc[dataframe['submission_time'] == dataframe['submission_time'].min()].compute()
print(f'Первые по дате подачи рецепты: \n{earliest_recipe}')

# Загружаем рецепты в базу данных 
database_connection_string = 'sqlite:///recipes.db'  # Строка подключения  
dataframe.to_sql('recipes', database_connection_string, if_exists='replace', index=False)  # Заменяем таблицу, если она существует
print("Данные успешно загружены в SQLite.")

median_cooking_time = dataframe['minutes'].median_approximate().compute()  # Вычисляем медиану времени приготовления
average_steps = dataframe['n_steps'].mean().compute()      # Вычисляем среднее количество шагов

# Загрузка данных из таблицы recipes с использованием строки подключения
loaded_dataframe = dd.read_sql_table('recipes', database_connection_string, index_col='id')

# Фильтрация данных
filtered_dataframe = loaded_dataframe[(loaded_dataframe['minutes'] < median_cooking_time) & (loaded_dataframe['n_steps'] < average_steps)]

# Сохраняем отфильтрованные данные в один CSV-файл
filtered_dataframe.to_csv('filtered_recipes.csv', single_file=True, index=False) 
print("Отфильтрованные рецепты сохранены в filtered_recipes.csv.")
