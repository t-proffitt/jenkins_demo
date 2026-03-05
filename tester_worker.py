import unittest
# Now we import the function AND the specific variables
from worker import add_numbers, NUM_1, NUM_2

class TestWorker(unittest.TestCase):
    def test_dynamic_numbers(self):
        # The test automatically uses whatever numbers you set in worker.py.
        # It adds them together and expects the answer to ALWAYS be 15.
        self.assertEqual(add_numbers(NUM_1, NUM_2), 15)

if __name__ == "__main__":
    unittest.main()
