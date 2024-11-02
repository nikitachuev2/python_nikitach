from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def multiply():
    # Получаем значения a, b и c из параметров запроса
    a = request.args.get('a', default=1, type=float)
    b = request.args.get('b', default=1, type=float)
    c = request.args.get('c', default=1, type=float)

    # Выполняем умножение
    result = a * b * c

    # Формируем ответ с описанием
    response = (
        "Добро пожаловать на сервер для умножения чисел!\n"
        "Этот сервер принимает три параметра: a, b и c, и вычисляет их произведение.\n"
        "Вы можете обращаться к серверу по адресу: http://127.0.0.1:5000/\n\n"
        "Как использовать функцию:\n"
        "1. Откройте браузер и в адресной строке введите адрес сервера: http://127.0.0.1:5000/\n"
        "2. Добавьте три параметра a, b и c в запрос. Например:\n"
        "   - Для умножения чисел 2, 3 и 4 введите: http://127.0.0.1:5000/?a=2&b=3&c=4\n"
        "3. Результат умножения будет отображен на странице.\n\n"
        "Примечания:\n"
        "- Параметры a, b и c могут быть любыми числами. Если вы не укажете их, по умолчанию они будут равны 1.\n"
        "- Вы можете менять значения параметров в URL, чтобы получать разные результаты.\n\n"
        f"Умножение чисел: {a} умножить на {b} умножить на {c} равно {result}."
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)