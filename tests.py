import unittest
from src.fib import fib

class test_fib(unittest.TestCase):
    def test_1(self):
        fib_gen = fib()
        res = [next(fib_gen) for _ in range(10)]
        self.assertEqual(len(res), 10)
        self.assertEqual(res, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_2(self):
        fib_gen = fib()
        res = [next(fib_gen) for _ in range(3)]
        self.assertEqual(len(res), 3)
        self.assertEqual(res, [1, 1, 2])

    def test_3(self):
        fib_gen = fib()
        res = [next(fib_gen) for _ in range(5)]
        self.assertEqual(len(res), 5)
        self.assertEqual(res, [1, 1, 2, 3, 5])

if __name__ == "__main__":
    unittest.main()