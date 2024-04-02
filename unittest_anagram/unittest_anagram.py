import unittest
from anagram.anagram.anagram import reverse_words

class TestReverseWords(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(reverse_words("abcd"), "dcba")

    def test_multiple_words(self):
        self.assertEqual(reverse_words("abcd efgh"), "dcba hgfe")

    def test_words_with_special_chars(self):
        self.assertEqual(reverse_words("a1bcd efg!h"), "d1cba hgf!e")

    def test_empty_input(self):
        self.assertEqual(reverse_words(""), "")

    def test_non_alpha_chars_only(self):
        self.assertEqual(reverse_words("!@#$%^"), "!@#$%^")

    def test_single_letter_word(self):
        self.assertEqual(reverse_words("a"), "a")

    def test_two_words(self):
        self.assertEqual(reverse_words("ab cd"), "ba dc")

    def test_word_with_non_alpha_char(self):
        self.assertEqual(reverse_words("a!"), "a!")


if __name__ == "__main__":
    unittest.main()
