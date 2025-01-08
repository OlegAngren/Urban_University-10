import time  # Для измерения времени и паузы
from time import sleep  # Для паузы
from threading import Thread  # Для работы с потоками


# Функция для записи слов в файл
def write_words(word_count, file_name):
    """
    Функция записывает указанное количество слов в файл с паузой между записями.

    :param word_count: количество слов для записи
    :param file_name: название файла
    """
    with open(file_name, "w") as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")  # Записываем строку в файл
            sleep(0.1)  # Пауза между записями
    print(f"Завершилась запись в файл {file_name}")


# Основная программа
if __name__ == "__main__":
    # Измеряем время выполнения функций
    start_time = time.time()

    # Последовательный вызов функций
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")

    end_time = time.time()
    print(f"Работа функций заняла {end_time - start_time:.2f} секунд")

    # Измеряем время выполнения потоков
    start_time_threads = time.time()

    # Создаем потоки
    threads = [
        Thread(target=write_words, args=(10, "example5.txt")),
        Thread(target=write_words, args=(30, "example6.txt")),
        Thread(target=write_words, args=(200, "example7.txt")),
        Thread(target=write_words, args=(100, "example8.txt")),
    ]

    # Запускаем потоки
    for thread in threads:
        thread.start()

    # Ждем завершения потоков
    for thread in threads:
        thread.join()

    end_time_threads = time.time()
    print(f"Работа потоков заняла {end_time_threads - start_time_threads:.2f} секунд")

