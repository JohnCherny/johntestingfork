import unittest
from challenge import longest_word

class TestLongestWord(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(longest_word("hello"), "hello")

    def test_simple_sentence(self):
        self.assertEqual(longest_word("the quick brown fox"), "quick")

    def test_punctuation(self):
        self.assertEqual(longest_word("Hello, world!"), "Hello")

    def test_multiple_longest(self):
        self.assertEqual(longest_word("cat dog bird"), "bird")

    def test_empty_string(self):
        self.assertEqual(longest_word(""), "")

    def test_spaces_only(self):
        self.assertEqual(longest_word("     "), "")

    def test_sentence_with_numbers(self):
        self.assertEqual(longest_word("I have 12345 and 678"), "12345")

    def test_mixed_punctuation(self):
        self.assertEqual(longest_word("Wow!!! That... is amazing"), "amazing")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            longest_word(123)

if __name__ == "__main__":
    unittest.main()
