import unittest

import sort


class test_sort(unittest.TestCase):
    def test_sort_1_1(self):
        self.assertEqual(sort.sort_1([3, -4, 5, 0, 1]), [5, -4, 3, 1, 0])

    def test_sort_1_2(self):
        self.assertEqual(sort.sort_1([3, -4, 4, 5, 0, 1, -1, 17]), [17, 5, -4, 4, 3, 1, -1, 0])

    def test_sort_1_3(self):
        self.assertEqual(sort.sort_1([0, -100, 100, 67, -67, 67, 99, 15, 16, -15]),
                         [-100, 100, 99, 67, -67, 67, 16, 15, -15, 0])

    def test_sort_2_1(self):
        self.assertEqual(sort.sort_2([3, -4, 5, 0, 1]), [5, -4, 3, 1, 0])

    def test_sort_2_2(self):
        self.assertEqual(sort.sort_2([3, -4, 4, 5, 0, 1, -1, 17]), [17, 5, -4, 4, 3, 1, -1, 0])

    def test_sort_2_3(self):
        self.assertEqual(sort.sort_2([0, -100, 100, 67, -67, 67, 99, 15, 16, -15]),
                         [-100, 100, 99, 67, -67, 67, 16, 15, -15, 0])


if __name__ == "__main__":
    unittest.main()
