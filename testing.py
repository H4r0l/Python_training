import unittest

class TestSum(unittest.TestCase):

    def test_sum_list(self):
        self.assertEqual(sum([6,6,6]), 18)

if __name__ == '__main__':
    unittest.main()