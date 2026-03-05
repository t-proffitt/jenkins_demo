import unittest
#import the function & specific variables
from worker import add_numbers, NUM_1, NUM_2

class TestWorker(unittest.TestCase):
    def test_dynamic_numbers(self):
        #test automatically uses whatever numbers are set in worker.py
        self.assertEqual(add_numbers(NUM_1, NUM_2), 15)
        #sum of NUM_1 & NUM_2 should =15

if __name__ == "__main__":
    unittest.main()
