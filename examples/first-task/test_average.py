import unittest
from average import average


class AverageTests(unittest.TestCase):
    def test_normal_values(self):
        self.assertEqual(average([2, 4, 6]), 4.0)

    def test_empty_values(self):
        self.assertEqual(average([]), 0.0)

    def test_negative_values(self):
        self.assertEqual(average([-2, -4]), -3.0)


if __name__ == '__main__':
    unittest.main()
