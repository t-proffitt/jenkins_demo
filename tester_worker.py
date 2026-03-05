import unittest
from worker import add_numbers

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_numbers(10, 5), 16)
    
    def test_add_negative(self):
        self.assertEqual(add_numbers(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()
