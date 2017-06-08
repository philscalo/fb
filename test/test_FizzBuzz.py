import unittest
from src.FizzBuzz import fizz_buzz


class test_fizz_buzz_assess(unittest.TestCase):
    def test_five_is_buzz(self):
        self.assertEqual(fizz_buzz(5), 'Buzz')


    def test_three_is_fizz(self):
        self.assertEqual(fizz_buzz(3), 'Fizz')


    def test_fifteen_is_fizzbuzz(self):
        self.assertEqual(fizz_buzz(15), 'FizzBuzz')


    def test_nineteen_is_nothing(self):
        self.assertEqual(fizz_buzz(19), 19)


if __name__ == '__main__':
    unittest.main()