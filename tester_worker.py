import unittest
from worker import add_numbers, NUM_1, NUM_2

class TestWorker(unittest.TestCase):
    def test_dynamic_numbers(self):
        actual_sum = add_numbers(NUM_1, NUM_2)
        
        u_error = f"The required sum is 15. {actual_sum} is unacceptable. Self Destruct."
        
        self.assertEqual(actual_sum, 15, u_error)
        #sum of NUM_1 & NUM_2 should =15
if __name__ == "__main__":
    unittest.main()
