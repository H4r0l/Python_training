import unittest

class TestSum(unittest.TestCase):

    def setUp(self):
        self.list = [2,2,2]

    def test_sum_list(self):
        self.assertEqual(sum(self.list), 6)

    def test_multiply_list(self):
        self.assertEqual((self.list[1]* self.list[2]), 4)

    @unittest.skip("skipping")
    def test_divide_list(self):
        self.assertAlmostEqual((self.list[0]/ self.list[1]), 1)

    def tearDown(self):
        del(self.list)



if __name__ == '__main__':
    unittest.main()