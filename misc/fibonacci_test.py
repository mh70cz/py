""" test fibonacci """
import unittest
import fibonacci as fib

class TestFib(unittest.TestCase):
    """ test basic functionality """

    fib_0_based_26 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
                      377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
                      28657, 46368, 75025]
    fib_1_based_26 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
                      377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
                      28657, 46368, 75025, 121393]

    def wrong_fake_method(self):
        pass

    def test_zero_based(self):
        self.assertEqual(fib.fib_runner(0, 26),
                         self.fib_0_based_26)
        self.assertEqual(fib.fib_runner(0, 26, fib.memo_fibonacci),
                         self.fib_0_based_26)
        self.assertEqual(fib.fib_runner(0, 26, fib.memo_decor_fibonacci),
                         self.fib_0_based_26)
        self.assertEqual(fib.fib_sequence(0, 26), self.fib_0_based_26)

    def test_one_based(self):
        self.assertEqual(fib.fib_runner(1, 27),
                         self.fib_1_based_26)
        self.assertEqual(fib.fib_runner(1, 27, fib.memo_fibonacci),
                         self.fib_1_based_26)
        self.assertEqual(fib.fib_runner(1, 27, fib.memo_decor_fibonacci),
                         self.fib_1_based_26)
        self.assertEqual(fib.fib_sequence(1, 27), self.fib_1_based_26)


    def test_wrong_input_type_exception(self):
        with self.assertRaises(fib.SanitizeInputError) as cm:
            fib.fib_runner("abc", 10)
        the_exception = cm.exception
        self.assertEqual(the_exception.args[0], "math.floor")

        with self.assertRaises(fib.SanitizeInputError):
            fib.fib_runner(1, "abc")
        the_exception = cm.exception
        self.assertEqual(the_exception.args[0], "math.floor")            

    def test_wrong_input_values(self):
        with self.assertRaises(fib.SanitizeInputError) as cm:
            fib.fib_runner(-1, 10)
        the_exception = cm.exception
        self.assertRegex(the_exception.args[0], "value")

        with self.assertRaises(fib.SanitizeInputError) as cm:
            fib.fib_runner(-2, 1)
        the_exception = cm.exception
        self.assertRegex(the_exception.args[0], "value")            

    def test_wrong_method(self):
        with self.assertRaises(fib.SanitizeInputError) as cm:
            fib.fib_runner(1, 10, self.wrong_fake_method())
        the_exception = cm.exception
        self.assertRegex(the_exception.args[0], "method")
