
import requests # Импортируем библиотеку requests для отправки HTTP-запросов

username = "octocat" # Задаём имя пользователя GitHub, по которому будем делать запрос

# Формируем URL запроса, подставляя имя пользователя вместо {username}
url = f"https://api.github.com/users/{username}" 

# Отправляем GET-запрос к API GitHub и получаем ответ
response = requests.get(url)

# Проверяем, что запрос выполнился успешно (код ответа 200 - "ОК")
if response.status_code == 200:
    # Преобразуем JSON-ответ в Python-словарь
    data = response.json()
    
    # Извлекаем из словаря нужные данные
    name = data["name"]
    login = data["login"]
    repos_count = data["public_repos"]
    
    # Выводим информацию на экран
    print(f"Name: {name}")
    print(f"Login: {login}")
    print(f"Repositories: {repos_count}")
else:
    # Если запрос не выполнился успешно, выводим сообщение об ошибке
    print(f"Error: {response.status_code} - {response.text}")
