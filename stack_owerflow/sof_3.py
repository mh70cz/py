#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 13:26:55 2018; @author: mh70
https://stackoverflow.com/questions/49716841/creating-new-arrays-based-on-unique-keys-and-condition-in-python
"""



from io import StringIO
import pandas as pd

txt = StringIO("""
A,B,C
9,1952,125
2,1994,69
3,1973,72
5,1992,85
1,1994,38
1,1994,95
4,1992,29
8,1984,94
""")

df = pd.read_csv(txt )

condition = (df["B"] >1980) & (df["B"] < 1989)
#condition = (df["B"] >1990) & (df["B"] < 2000)
df_cond = df[condition]

df_uniq = df_cond.drop_duplicates('A', keep=False)
df_uniq_keep_first = df_cond.drop_duplicates('A', keep="first")
df_uniq_keep_last = df_cond.drop_duplicates('A', keep="last")

sum_dupl = df_cond["C"].sum()
sum_uniq = df_uniq["C"].sum()
sum_uniq_keep_first = df_uniq_keep_first["C"].sum()
sum_uniq_keep_last = df_uniq_keep_last["C"].sum()

print("sum with duplicates  : " + str(sum_dupl))            #316
print("sum pure unique      : " + str(sum_uniq))            #183
print("sum unique keep first: " + str(sum_uniq_keep_first)) #221 
print("sum unique keep last : " + str(sum_uniq_keep_last))  #278
