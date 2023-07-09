import random

def generate_unique_random_numbers(length, start, end):
    if length > (end - start + 1):
        raise ValueError("Длина списка больше возможного диапазона уникальных чисел.")

    random_numbers = random.sample(range(start, end + 1), length)
    return map(str, random_numbers)

def generate_test(size = 20000, start = 1, end = 5000):
    """
    Функция создает файл `structure.txt` с указанным количеством чисел
    
    size: Количество чисел в файле
    start: левая граница генерируемых чисел
    end: правая граница генерируемых чисел
    """
    # генерируем тело бинарного дерева поиска по заданным параметрам
    # так как все значения в дереве уникальные - делаем множество
    raw_list = generate_unique_random_numbers(size, start, end)

    with open("structure.txt", "w", encoding="UTF-8") as file:
        file.write(" ".join(raw_list))