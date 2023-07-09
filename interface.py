import time
import random
import sys

from algorithm import *
import generate_structure as gs

if "-g" in sys.argv:
    START_TIME = time.time()
    print("Генерируем структуру в файл...", end="")
    if "-hard" in sys.argv:
        gs.generate_test(2000000, 1, 10000000)
    else:
        a1, a2, a3 = random.randint(100, 1000), 1, random.randint(300, 2000)
        print(f"""Параметры структуры:
    Количество статей: {a1}
    Минимальный номер: {a2}
    Максимальный номер: {a3}
""")
        gs.generate_test(a1, a2, a3)
    print("Успешно за", round(time.time() - START_TIME, 3), "секунд!")

START_TIME = time.time()
print("Читаем файл...", end="")
with open("structure.txt", "r", encoding="UTF-8") as file:
    DATA = list(map(int, file.read().split()))
print("Успешно за", round(time.time() - START_TIME, 3), "секунд!")

print("Формируем дерево...", end="")
root = build_bst(DATA)
print("Успешно за", round(time.time() - START_TIME, 3), "секунд!")

input_num = 1

cache = dict()
it = InorderTraversal()

while input_num:
    try:
        input_num = int(input("Введите номер статьи затрат (enter для выхода)>>>"))
    except ValueError:
        quit()

    # засекаем время обхода дерева
    START_TIME = time.time()

    print("  Результат:", it.get(root, input_num), "(", round(time.time() - START_TIME, 3), "секунд )")
