""" test throw a custom exception from try / except """
import unittest

# https://stackoverflow.com/questions/16414744/python-exception-chaining

#  PEP 3134 has two situations for chaining: one where error handling
# code results in another exception being raised,
# and the other where an exception was deliberately
# translated to a different exception

def mthd_simple():
    """ throw a custom exception form except no chaining"""
    try:
        x = 1/0
    except:
        raise MyException("no chaining")

def mthd_chain():
    """ throw a custom exception from except with chaning"""
    try:
        x = 1/0
    except Exception as e:
        raise MyException("chaining") from e

def mthd_chain_fn():
    """ throw a custom exception from except with chaning from None """
    try:
        x = 1/0
    except Exception:
        raise MyException("chaining from None") from None


def show_ex_simple():
    print("\nthrow a custom exception form except no chaining:\n")
    mthd_simple()

def show_ex_chain():
    print("\nthrow a custom exception from except with chaining:\n")
    mthd_chain()

def show_ex_chain_fn():
    print("\nthrow a custom exception from except with chaining from None:\n")
    mthd_chain_fn()

class MyException(Exception):
    pass


class TestEx(unittest.TestCase):
    """ ut """

    def test_MyEx_simple(self):
        with self.assertRaises(MyException) as cm:
            mthd_simple()
        the_exception = cm.exception
        self.assertRegex(the_exception.args[0], "no chaining")

    def test_MyEx_chain(self):
        with self.assertRaises(MyException) as cm:
            mthd_chain()
        the_exception = cm.exception
        self.assertRegex(the_exception.args[0], "^chaining")

    def test_MyEx_chain_fn(self):
        with self.assertRaises(MyException) as cm:
            mthd_chain_fn()
        the_exception = cm.exception
        self.assertRegex(the_exception.args[0], "chaining from None")

unittest.main()
#show_ex_chain_fn()
