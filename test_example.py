import unittest
from example import fizzbuzz


if __name__ == '__main__':
    unittest.main()


class TestFizzBuzz(unittest.TestCase):

    def test_one(self):
        self.assertEqual(fizzbuzz(1), [1])

    def test_two(self):
        self.assertEqual(fizzbuzz(2), [1,2])

    def test_three(self):
        self.assertEqual(fizzbuzz(3), [1,2, 'Fizz'])

    def test_five(self):
        self.assertEqual(fizzbuzz(5), [1,2, 'Fizz', 4, 'Buzz'])

    def test_ten(self):
        self.assertEqual(fizzbuzz(10), [1,2, 'Fizz', 4, 'Buzz', 'Fizz', 7,8,'Fizz', 'Buzz'])

    def test_fifteen(self):
        self.assertEqual(fizzbuzz(15), [1,2, 'Fizz', 4, 'Buzz', 'Fizz', 7,8,'Fizz', 'Buzz', 11,'Fizz',13,14,'FizzBuzz'])

    def test_zero(self):
        self.assertEqual(fizzbuzz(0), [])

    def test_bad_input(self):
        self.assertEqual(fizzbuzz('bad input'), [])