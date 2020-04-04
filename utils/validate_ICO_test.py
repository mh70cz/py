""" test validací IČO """
import unittest
from validate_ICO import validate


class TestICO(unittest.TestCase):
    """ ut """

    def test_correct_check_digit_int(self):
        list_ico = [27600297, 25596641, 69663963, 51, 43]
        for ico in list_ico:
            self.assertTrue(validate(ico), ico)


    def test_correct_check_digit_string(self):
        list_ico = ["27600297", "25596641", "69663963",
                    "51", "43", "00000051", "00000043"
                   ]
        for ico in list_ico:
            self.assertTrue(validate(ico), ico)

    def test_wrong_check_digit(self):
        list_wrong_ico = [41, 25196641, 69163963]
        for ico in list_wrong_ico:
            self.assertFalse(validate(ico), ico)

    def test_wrong_format(self):
        list_wrong_format_ico = [123456789, 1, "1", 987654321,
                                 "a1234567", "123a4567", "1234567a",
                                 "1234 567", "51 12345", "12345 51",
                                 -12345678, "-12345678", -1234567, "-1234567"
                                ]
        for ico in list_wrong_format_ico:
            self.assertIsNone(validate(ico), ico)

    def test_wrong_data_type(self):
        list_wrong_data_type_ico = [True, False, None, "NaN", (12345678, 87654321)]
        for ico in list_wrong_data_type_ico:
            self.assertIsNone(validate(ico), ico)

    def test_strip_input(self):
        list_nonstripped_ico = [" 25596641 ", "   69663963", "27600297  "]
        # IČO výše jsou validní
        for ico in list_nonstripped_ico:
            self.assertTrue(validate(ico), ico)



