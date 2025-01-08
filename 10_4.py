import threading  # Для работы с потоками
from queue import Queue  # Для создания очереди гостей
from random import randint  # Для генерации случайного времени
from time import sleep  # Для паузы в потоке

# Класс Table
class Table:
    def __init__(self, number):
        """
        Создание стола с номером и без гостя.
        """
        self.number = number  # Номер стола
        self.guest = None  # Гость за столом, изначально None

# Класс Guest
class Guest(threading.Thread):
    def __init__(self, name):
        """
        Создание гостя с именем.
        """
        super().__init__()
        self.name = name  # Имя гостя

    def run(self):
        """
        Имитация времени пребывания гостя за столом.
        """
        eating_time = randint(3, 10)  # Время "еды" от 3 до 10 секунд
        sleep(eating_time)  # Задержка для имитации
        print(f"{self.name} покушал(-а) за {eating_time} секунд(ы).")

# Класс Cafe
class Cafe:
    def __init__(self, *tables):
        """
        Создание кафе с заданными столами.
        """
        self.tables = list(tables)  # Список столов
        self.queue = Queue()  # Очередь гостей

    def guest_arrival(self, *guests):
        """
        Метод прибытия гостей.
        """
        for guest in guests:
            for table in self.tables:
                if table.guest is None:  # Если стол свободен
                    table.guest = guest  # Сажаем гостя за стол
                    guest.start()  # Запускаем поток гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            else:
                # Если свободных столов нет, добавляем гостя в очередь
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        """
        Метод обслуживания гостей.
        """
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    # Если гость за столом закончил приём пищи
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол

                    if not self.queue.empty():  # Если есть гости в очереди
                        next_guest = self.queue.get()  # Берём следующего гостя
                        table.guest = next_guest  # Сажаем его за стол
                        next_guest.start()  # Запускаем поток гостя
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

# Тестирование программы
if __name__ == "__main__":
    # Создаём столы
    tables = [Table(number) for number in range(1, 6)]

    # Список имён гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]

    # Создаём гостей
    guests = [Guest(name) for name in guests_names]

    # Создаём кафе с нашими столами
    cafe = Cafe(*tables)

    # Принимаем гостей
    cafe.guest_arrival(*guests)

    # Обслуживаем гостей
    cafe.discuss_guests()
