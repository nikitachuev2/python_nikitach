
class Room:  # Определяем класс Room для представления комнаты в отеле.
    def __init__(self, room_number, max_guests, price_per_night):  # Инициализация атрибутов комнаты.
        self.room_number = room_number  # Номер комнаты.
        self.max_guests = max_guests  # Максимальное количество гостей в комнате.
        self.price_per_night = price_per_night  # Цена за ночь.
        self.is_available = True  # Комната доступна по умолчанию.

    def book(self):  # Метод для бронирования комнаты.
        if self.is_available:  # Проверка, доступна ли комната.
            self.is_available = False  # Устанавливаем комнату как занятую.
            print(f"Room {self.room_number} booked.")  # Сообщение о бронировании.
        else:
            print(f"Room {self.room_number} is not available.")  # Сообщение о недоступности.

    def free(self):  # Метод для освобождения комнаты.
        self.is_available = True  # Устанавливаем комнату как свободную.
        print(f"Room {self.room_number} is now free.")  # Сообщение о свободной комнате.


class Luxury(Room):  # Класс Luxury наследует от Room.
    def __init__(self, room_number, max_guests, price_per_night, has_balcony, has_mini_bar):
        super().__init__(room_number, max_guests, price_per_night)  # Инициализация родительских атрибутов.
        self.has_balcony = has_balcony  # Наличие балкона.
        self.has_mini_bar = has_mini_bar  # Наличие мини-бара.


class Standard(Room):  # Класс Standard наследует от Room.
    def __init__(self, room_number, max_guests, price_per_night, beds_count):
        super().__init__(room_number, max_guests, price_per_night)  # Инициализация родительских атрибутов.
        self.beds_count = beds_count  # Количество кроватей в комнате.


class Economy(Standard):  # Класс Economy наследует от Standard.
    def __init__(self, room_number, max_guests, price_per_night, beds_count):
        super().__init__(room_number, max_guests, price_per_night, beds_count)  # Инициализация родительских атрибутов.
        self.beds_available = beds_count  # Доступные кровати.

    def book(self, guest_count):  # Метод для бронирования с учетом количества гостей.
        if self.is_available and self.beds_available >= guest_count:
            self.beds_available -= guest_count  # Уменьшаем доступные кровати.
            if self.beds_available == 0:
                self.is_available = False  # Если кровати закончились, устанавливаем комнату как недоступную.
            print(f"Room {self.room_number} booked for {guest_count} guests.")
        else:
            print(f"Room {self.room_number} is not available for {guest_count} guests.")

    def free(self, guest_count):  # Метод для освобождения комнаты с учетом количества гостей.
        self.beds_available += guest_count  # Увеличиваем доступные кровати.
        self.is_available = True  # Устанавливаем комнату как свободную.
        print(f"Room {self.room_number} is now free for {guest_count} guests.")


class Guest:  # Класс Guest для представления гостя.
    def __init__(self, name, phone, booking_id):
        self.name = name  # Имя гостя.
        self.phone = phone  # Телефон гостя.
        self.booking_id = booking_id  # Идентификатор бронирования.


class Hotel:  # Класс Hotel для представления отеля.
    def __init__(self):
        self.rooms = []  # Список комнат в отеле.

    def add_room(self, room):  # Метод для добавления комнаты в отель.
        self.rooms.append(room)  # Добавление комнаты в список.

    def find_rooms_for_guests(self, guest_count):  # Метод для поиска доступных комнат для гостей.
        return [room for room in self.rooms if room.is_available and room.max_guests >= guest_count]

    def all_available_rooms(self):  # Метод для получения всех доступных комнат.
        return [room for room in self.rooms if room.is_available]


def main():  # Основная функция программы.
    hotel = Hotel()  # Создание экземпляра отеля.
    while True:  # Бесконечный цикл для добавления комнат.
        room_type = input("Введите тип номера (Luxury/Standard/Economy): ").strip().lower()
        room_number = input("Введите номер комнаты: ")
        max_guests = int(input("Введите максимальное количество гостей: "))
        price_per_night = float(input("Введите цену за ночь: "))

        if room_type == "luxury":
            has_balcony = input("Есть ли балкон? (да/нет): ").strip().lower() == "да"
            has_mini_bar = input("Есть ли мини-бар? (да/нет): ").strip().lower() == "да"
            room = Luxury(room_number, max_guests, price_per_night, has_balcony, has_mini_bar)

        elif room_type == "standard":
            beds_count = int(input("Введите количество кроватей: "))
            room = Standard(room_number, max_guests, price_per_night, beds_count)

        elif room_type == "economy":
            beds_count = int(input("Введите количество кроватей: "))
            room = Economy(room_number, max_guests, price_per_night, beds_count)

        else:
            print("Неверный тип номера. Попробуйте снова.")
            continue

        hotel.add_room(room)

        another = input("Хотите добавить еще одну комнату? (да/нет): ").strip().lower()
        if another != "да":
            break

    while True:  # Бесконечный цикл для ввода данных гостя.
        guest_name = input("Введите полное имя гостя: ")
        guest_phone = input("Введите номер телефона гостя: ")
        booking_id = input("Введите идентификатор бронирования: ")

        guest = Guest(guest_name, guest_phone, booking_id)  # Создание экземпляра Guest с введенными данными.

        guest_count = int(input("Введите количество гостей для бронирования: "))
        
        available_rooms = hotel.find_rooms_for_guests(guest_count)
        
        if available_rooms:
            for room in available_rooms:
                print(f"Доступная комната: {room.room_number}, Цена за ночь: {room.price_per_night}")
                
            selected_room_number = input("Введите номер выбранной комнаты для бронирования: ")
            selected_room = next((room for room in available_rooms if room.room_number == selected_room_number), None)
            
            if selected_room:
                if isinstance(selected_room, Economy):
                    selected_room.book(guest_count)
                else:
                    selected_room.book()
                print(f"Бронирование успешно для {guest.name}.")
            else:
                print("Комната не найдена.")
        else:
            print("Нет доступных комнат для указанного количества гостей.")

        another_guest = input("Хотите добавить еще одного гостя? (да/нет): ").strip().lower()
        if another_guest != "да":
            break


if __name__ == "__main__":  # Проверка на выполнение скрипта как основной программы.
    main()  # Вызов основной функции программы.
