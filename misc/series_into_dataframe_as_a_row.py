# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 16:19:57 2018; @author: mh70
pandas append series into dataframe as a row 
"""

import pandas as pd

df = pd.DataFrame([[1,2],[3,4]],columns=['A','B'])
s = pd.Series(["alpha","beta"],index=['A','B'])

print("df :")
print(df)
print("\ns :")
print(s)

df_out = df.append(s, ignore_index=True)
print(df_out)