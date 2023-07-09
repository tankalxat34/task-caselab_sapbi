import unittest
import random
from unittest import TestCase
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithm import build_bst, InorderTraversal
from generate_structure import generate_test


class Testing(TestCase):
    def random_tst(self, size: int, left: int, right: int, test_count: int = 10):
        generate_test(size, left, right)

        it = InorderTraversal()
        for x in range(test_count):
            with open("structure.txt", "r", encoding="UTF-8") as file:
                DATA = list(map(int, file.read().split()))

            DATA_SORTED = sorted(DATA)
            input_num = random.randint(DATA_SORTED[0], DATA_SORTED[-1])

            root = build_bst(DATA)

            # создаем переменную для правильного ответа
            right_answer = input_num

            # пока правильный ответ больше текущего числа в дереве
            # увеличим индекс. Так мы придем к действительно правильному ответу.
            i = 0
            while right_answer > DATA_SORTED[i]:
                i += 1
            
            try:
                # поправка: так как по условию задачи ответ должен быть больше, чем заданное число, то в случае,
                # когда заданное число уже есть в дереве, нам надо вернуть ближайшее бОльшее за ним число.
                right_answer = DATA_SORTED[i] if right_answer not in DATA_SORTED else DATA_SORTED[i+1]
            except IndexError:
                # если выбрано последнее число и больше него ничего нет - ответ не найден
                right_answer = -1

            # при желании во время тестирования может выводиться информация на экран
#             print(f"""Random test #{x}
#     cin: {input_num}
#     cout: {it.get(root, input_num)}
#     answer: {right_answer}
# """)
            self.assertEqual(it.get(root, input_num), right_answer)

    def test_random_small(self):
        return self.random_tst(20, 1, 100)
    
    def test_random_small2(self):
        return self.random_tst(200, 1, 200)
    
    def test_random_random(self):
        return self.random_tst(random.randint(100, 1000), 1, random.randint(300, 2000))
    
    def test_random_large(self):
        return self.random_tst(200000, 1, 10000000)
    
    def test_random_edge_cases(self):
        return self.random_tst(2000000, 1, 10000000, 3)

if __name__ == "__main__":
    unittest.main()