import unittest
from src.FizzBuzz import fizz_buzz


class test_fizz_buzz_assess(unittest.TestCase):
    def test_five_is_buzz(self):
        self.assertEqual(fizz_buzz(5), 'Buzz')


if __name__ == '__main__':
    unittest.main()