"""Validate Czech PIN, validuj rodné číslo"""

import random
import datetime

def validate(rc):

    rc = sanitize_input(rc)
    if rc is None:
        return None
    if not check_date(rc):
        return False
    if len(rc) < 10:
        if int(rc[:1]) > 54:
            return False
    else:
        check = calculate_check_digit(rc[:-1])
        if rc[-1] == str(check):
            return True
        else:
            return False

def calculate_check_digit(sub_rc):
    """vypocitej kontrolni cislici"""
    if len(sub_rc) < 1 or len(sub_rc) > 9:
        return None
    sub_rc = int(sub_rc)
    remainder = sub_rc % 11
    if remainder == 10:
        check = 0
    else:
        check = remainder
    return check

def check_date(rc):
    year = int(rc[:2])
    if len(rc) == 9:
        year += 1900
    elif year > 54:
        year += 1900
    else:        
        year += 2000
    month = int(rc[2:4])

    #ženy mají k měsíci narození připočteno 50
    if month > 50 and month < 63:
        month -= 50

    # Od roku 2004 (zák. 53/2004 Sb.) je navíc zavedena možnost v případě,
    # že jsou v některý den vyčerpána všechna platná čtyřčíslí,
    # použít alternativní rodné číslo, kde se k číslu měsíce přičte ještě 20
    # (u žen tedy celkem 70).
    if month > 20 and month < 33 and year >= 2004:
        month -= 20
    if month > 70 and month < 83 and year >= 2004:
        month -= 70
     
    day = int(rc[4:6])
    # cizinci ??? nezjištěno
    #if day < 50 and day < 63:
    #    day -= 50

    try:
        newDate = datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False

def sanitize_input(rc):
    """ if possible return a string of from 9 to 10 digits, else None"""
    if isinstance(rc, int):
        if rc > 999_999_999_9 or rc < 999_999_999:
            return None
        else:
            return str(rc)

    if isinstance(rc, str):
        rc = rc.strip()
        if len(rc) > 8:
            if rc[6] == "/":
                rc = rc[:6] + rc[7:]
            if len(rc) > 10:
                return None
            if rc.isdigit():
                return rc
            else:
                return None


def generate_exceptional_rc(n=1):
    list_exc_rc = []

    while True:
        year = str(random.randrange(55, 86)).rjust(2, "0")
        month = str(random.randrange(1, 13)).rjust(2, "0")
        day = str(random.randrange(1, 29)).rjust(2, "0")
        serialn = str(random.randrange(1, 1000)).rjust(3, "0")

        mod = int(year + month + day + serialn) % 11

        if mod == 10:
            list_exc_rc.append(year + month + day + serialn + "0")
            if len(list_exc_rc) == n:
                return list_exc_rc
