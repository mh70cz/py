
import unittest

def is_palindrome(number):
    str_num = str(number)
    
    str_num_len = len(str_num)
    end_left = str_num_len // 2
    start_right = str_num_len - end_left + 1
    
    left = str_num[0:end_left]
    right = str_num[start_right - 1:]
    
    if left == right[::-1] :
        return True
    else:
        return False


class TestPalindrome(unittest.TestCase):
    
    def test_even_palindrome(self):
        lst = [123321, 23566532, 1111, 22]
        for n in lst:
            self.assertTrue(is_palindrome(n))

    def test_even_not_palindrome(self):
        lst = [123123, 11232311, 12, ]            
        for n in lst:
            self.assertFalse(is_palindrome(n))

    def test_odd_palindrome(self):
        lst = [1234321, 666,  656, 1]
        for n in lst:
            self.assertTrue(is_palindrome(n))

    def test_odd_not_palindrome(self):
        lst = [1234328, 645,]            
        for n in lst:
            self.assertFalse(is_palindrome(n))

unittest.main()            