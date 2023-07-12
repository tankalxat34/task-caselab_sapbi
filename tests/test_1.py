import unittest
from unittest import TestCase
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithm import build_bst, InorderTraversal


class Testing(TestCase):
    def test_ex1(self):
        root = build_bst([10, 5, 7, 16, 13, 2, 20])

        it = InorderTraversal()
        self.assertEqual(it.get(root, 15), 16)
        self.assertEqual(it.get(root, 16), 20)
        self.assertEqual(it.get(root, 17), 20)
        self.assertEqual(it.get(root, 1), 2)
        self.assertEqual(it.get(root, 0), 2)

    def test_notfound(self):
        root = build_bst([10, 5, 7, 16, 13, 2, 20])

        it = InorderTraversal()
        self.assertEqual(it.get(root, 21), -1)
        
    def test_ex2(self):
        root = build_bst([500, 450, 420, 470, 1, 1024, 510, 505, 790])

        it = InorderTraversal()
        self.assertEqual(it.get(root, 470), 500)
        self.assertEqual(it.get(root, 500), 505)

    def test_ex3(self):
        root = build_bst([50, 48, 30, 28, 45, 215, 49, 652, 104, 1, 512])

        it = InorderTraversal()
        self.assertEqual(it.get(root, 215), 512)
        self.assertEqual(it.get(root, 2), 28)
        self.assertEqual(it.get(root, 1), 28)
        self.assertEqual(it.get(root, 48), 49)
        self.assertEqual(it.get(root, 38), 45)


if __name__ == "__main__":
    unittest.main()