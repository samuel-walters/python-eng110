from scrabble import Scrabble
from string import ascii_lowercase
from string import ascii_uppercase
import unittest

class Scrabbletests(unittest.TestCase):
    obj = Scrabble()
    # always add test at the start of the testing functions
    def test_value_checks(self):
        assert self.obj.get_value_count("a") == 1
        assert self.obj.get_value_count("Sam") == 5
        assert self.obj.get_value_count("aaiwefjiwajfawhzzzffawfea") == 96
    def test_letter_in_value_dict(self):
        #self.assertIn("Z", self.obj.value_dict)
        #self.assertIn("G", self.obj.value_dict)
        for upper_case_letter in ascii_uppercase:
            self.assertIn(upper_case_letter, self.obj.value_dict)
    def test_not_none(self):
        self.assertIsNotNone(self.obj.get_value_count("uiwajfejaifj"))
    def test_invalid_input(self):
        self.assertEqual("Please ensure your word only has alphabet characters.", self.obj.get_value_count("jwef jwf ''' ;;;; "))
    def test_no_lowercase_letters(self):
        for lower_case_letter in ascii_lowercase:
            self.assertNotIn(lower_case_letter, self.obj.value_dict)