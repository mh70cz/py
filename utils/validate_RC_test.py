""" test validací RČ """
import unittest
from validate_RC import validate

class TestRC(unittest.TestCase):
    """ ut """

    def test_correct_check_digit_int(self):
        list_rc = [7003150044, 1411281014, 7662150892]
        for rc in list_rc:
            self.assertTrue(validate(rc), rc)

    def test_correct_check_digit_str(self):
        list_rc = ["7003150044", "1411281014", "7662150892", "0002291234",
                   "700315/0044", "141128/1014", "766215/0892"]
        for rc in list_rc:
            self.assertTrue(validate(rc), rc)
            
    def test_correct_check_digit_after2004_add20_or_70_str(self):
        list_rc = ["0424158526", "0474158531", "1381098521", "1331098527" ]
        for rc in list_rc:
            self.assertTrue(validate(rc), rc)            



    def test_correct_exc_rc_check_digit_int(self):
        """
        výjimka: pokud je zbytek po dělení devítimístného čísla roven deseti 
        (a neexistuje tedy žádná kontrolní číslice, která by splňovala předchozí podmínku), 
        jako kontrolní číslice se použije nula (a celé rodné číslo pak dělitelné jedenácti není).
        """
        list_rc = [7012115760, 7203045070, 6909107360, 6306258080,
                   7206251900, 5711193280, 5905250330, 6705026780,
                   8105183670, 5904225240]
        for rc in list_rc:
            self.assertTrue(validate(rc), rc)

    def test_correct_exc_rc_check_digit_str(self):
        list_rc = ['6412161020', '6307249620', '6909156310', '8111246210',
                   '7512116470', '8412123270', '640528/8110', '581124/0370',
                   '770817/4090', '571221/0670']
        for rc in list_rc:
            self.assertTrue(validate(rc), rc)

    def test_wrong_check_digit_int(self):
        list_rc = [7003150045, 1411281013, 7662150890, 6909107361, 5904225249]
        for rc in list_rc:
            self.assertFalse(validate(rc), rc)

    def test_wrong_check_digit_str(self):
        list_rc = ["7003150045", "1411281013", "7662150890",
                   "6412161021", "6307249629"]
        for rc in list_rc:
            self.assertFalse(validate(rc), rc)

    def test_wrong_date(self):
        list_rc = ['7113011235', '7202301238', '7363113219', '7754318528',
                   '530230753', '131320753', '256931/852', '266611/951', '275431/456']
        for rc in list_rc:
            self.assertFalse(validate(rc), rc)

    def test_wrong_format(self):
        list_rc = ["700/3150044", "14a1128101", "7662150892a", 123456789123,
                   "12345678"]
        for rc in list_rc:
            self.assertIsNone(validate(rc), rc)

    def test_wrong_data_type(self):
        list_rc = [True, False, None, "NaN", (7003150044, 1411281014)]
        for rc in list_rc:
            self.assertIsNone(validate(rc), rc)
           