#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 17:32:33 2017

@author: mh
"""

import csv
import datetime
import bs_5


def save_to_file(fname, list_to_parse):
    with open(fname, "w", newline="", encoding="utf-8") as csvfile:
        csv_out = csv.writer(csvfile)
        csv_out.writerow(["link", "link_text", "txt", "site", "area"])

        for row in list_to_parse:
            csv_out.writerow(row)


def read_from_file(fname):
    read_list = list()
    with open(fname, newline="", encoding="utf-8") as csvfile:
        csv_in = csv.reader(csvfile)
        next(csv_in)  # gets the first line
        for row in csv_in:
            t = tuple(row)
            read_list.append(t)
    return read_list


def returnNotMatches(a, b):
    return [[x for x in a if x not in b], [x for x in b if x not in a]]


def main():
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    # home = "/home/mh/mypy/spyder/autumn_walks"
    # home ="c:/Users/m.houska/OneDrive/scripts/mypy/spyder"
    fname = "./data/idnes+lidovky" + today + ".csv"
    # fname = home + "/data/idnes+lidovky" + today + ".csv"
    parsed_info_list = bs_5.parse()
    save_to_file(fname, parsed_info_list)
    read_list = read_from_file(fname)
    not_match = returnNotMatches(parsed_info_list, read_list)
    print(not_match)


main()
