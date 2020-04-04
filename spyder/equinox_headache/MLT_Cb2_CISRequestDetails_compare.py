# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 10:28:04 2017

@author: mh70
"""

diff_lst = list()

row = dict()
row_test = dict()
row_diff = dict()

scr_list = data_src
conn_list = data_src_test

for idx, x in enumerate(scr_list):
    
    row = scr_list[idx] 
    #row_test = response_lst_test[idx]
    row_test = conn_list[idx]
    row_diff = dict()
    for key in row.keys():
        val = row[key]
        val_test = row_test[key]
        if not(val.strip() == val_test.strip()):
            row_diff[key] = (val, val_test)
    diff_lst.append(row_diff)
        