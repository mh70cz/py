"""Validate Czech registration number ICO, validuj IČO """

import re

def validate(ico):
    """Validate ICO - returns
    True is check digit is OK,
    False if check digit is NOT OK,
    None if format of IČO is not valid"""

    ico = sanitize_input(ico)
    if ico is None:
        return None
    check = calculate_check_digit(ico[:-1])
    if str(check) == ico[-1]:
        return True
    else:
        return False

def calculate_check_digit(sub_ico):
    """ vypocitej kontrolni cislici"""
    sub_ico = str(sub_ico)
    if len(sub_ico) < 1 or len(sub_ico) > 7:
        return None
    check_count = 0
    for idx in range(1, len(sub_ico) + 1):
        check_count += (idx + 1) * int(sub_ico[-1 * (idx)])
        # prvni z cislice zprava * 2 + druha cislice zprava * 3 + ... + sedma cislice zprava * 8
    remainder = check_count % 11
    if remainder == 0:
        check = 1
    elif remainder == 1:
        check = 0
    else:
        check = 11 - remainder
    return check

def sanitize_input(ico):
    """ if possible return a string of up to 8 digits, else None"""
    if isinstance(ico, int):
        ico = str(ico)
    if not isinstance(ico, str):
        return None
    ico = ico.strip()
    if len(ico) < 2 or len(ico) > 8:
        return None
    if not re.match("^[0-9]+$", ico):
        return None
    return ico
