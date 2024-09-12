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
        self.status = 'свободен'  # по умолчанию номер свободен
        self.hotel = hotel  

    def change_status(self):
        self.status = 'занят' if self.status == 'свободен' else 'свободен'

    def is_available(self):
        return self.status == 'свободен'

    def __str__(self):
        return f"Номер {self.number}: {self.category}, Мест: {self.capacity}, Статус: {self.status}, Отель: {self.hotel.name}"



class Hotel:
    def __init__(self, name: str, region: str):
        self.name = name
        self.region = region
        self.rooms = []  # Список номеров в отеле

    def add_room(self, number: str, category: str):
        room = Room(number, category, self)
        self.rooms.append(room)

    def change_room_status(self, room_number: str):
        for room in self.rooms:
            if room.number == room_number:
                room.change_status()
                print(f"Статус номера {room_number} изменен на {room.status}.")
                return
        print(f"Номер {room_number} не найден в отеле.")

    def get_available_rooms(self):

        return [room for room in self.rooms if room.is_available()]

    def __str__(self):
        return f"Отель {self.name}, Регион: {self.region}, Номера: {len(self.rooms)}"




# Создаем два отеля
hotel1 = Hotel("Отель 1", "Регион 1")
hotel2 = Hotel("Отель 2", "Регион 2")

# Добавляем номера в первый отель
hotel1.add_room("101", "Стандарт")
hotel1.add_room("102", "Люкс")
hotel1.add_room("103", "Апартаменты")

# Добавляем номера во второй отель
hotel2.add_room("201", "Стандарт")
hotel2.add_room("202", "Люкс")
hotel2.add_room("203", "Апартаменты")

# Просмотр информации об отелях и номерах
print(hotel1)
for room in hotel1.rooms:
    print(room)

print("\n", hotel2)
for room in hotel2.rooms:
    print(room)

# Изменяем статус одного из номеров 
hotel1.change_room_status("101")

# доступных номеров в первом отеле
print("\nСвободные номера в Отеле 1:")
for room in hotel1.get_available_rooms():
    print(room)
