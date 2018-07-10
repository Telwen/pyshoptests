def is_even(number):
    return number % 2


import unittest


class DefTest(unittest.TestCase):

    def test_even_basic(self):
        res = is_even(2)
        self.assertEqual(res, True)

    def test_odd_basic(self):
        res = is_even(5)
        self.assertEqual(res, False)

    def test_even_nagative(self):
        res = is_even(-4)
        self.assertEqual(res, True)

    def test_odd_nagative(self):
        res = is_even(-9)
        self.assertEqual(res, False)



if __name__ == '__main__':
    unittest.main()
