class Room:
    CATEGORY_CAPACITY = {
        'Стандарт': 2,
        'Люкс': 2,
        'Апартаменты': 4
    }

    def __init__(self, number: str, category: str, hotel: 'Hotel'):
        self.number = number
        self.category = category
        self.capacity = self.CATEGORY_CAPACITY.get(category, 2)
        self.status = 'свободен'  # По умолчанию номер свободен
        self.hotel = hotel  # Ссылка на объект отеля

    def change_status(self):
        """Меняет статус номера на противоположный"""
        self.status = 'занят' if self.status == 'свободен' else 'свободен'

    def is_available(self):
        """Проверка, свободен ли номер"""
        return self.status == 'свободен'

    def __str__(self):
        return f"Номер {self.number}: {self.category}, Мест: {self.capacity}, Статус: {self.status}, Отель: {self.hotel.name}"



class Hotel:
    def __init__(self, name: str, region: str):
        self.name = name
        self.region = region
        self.rooms = []  # Список номеров в отеле

    def add_room(self, number: str, category: str):
        """Добавление номера в отель"""
        room = Room(number, category, self)
        self.rooms.append(room)

    def change_room_status(self, room_number: str):
        """Меняет статус номера по его номеру"""
        for room in self.rooms:
            if room.number == room_number:
                room.change_status()
                print(f"Статус номера {room_number} изменен на {room.status}.")
                return
        print(f"Номер {room_number} не найден в отеле.")

    def get_available_rooms(self):
        """Возвращает список свободных номеров"""
        return [room for room in self.rooms if room.is_available()]

    def __str__(self):
        return f"Отель {self.name}, Регион: {self.region}, Номера: {len(self.rooms)}"

