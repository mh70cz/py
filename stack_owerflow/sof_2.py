# -*- coding: utf-8 -*-
"""
reply to:
https://stackoverflow.com/questions/49651170/python-calculate-median-value-of-different-dataframes/49652980    
"""
import pandas as pd

df_a = pd.read_csv('./a/merged.txt')
df_b = pd.read_csv('./b/merged.txt')

column_names = ["stat","a","b","c","d"]

df_a.columns = column_names
df_b.columns = column_names

df_combined = pd.concat([df_a, df_b])
med = df_combined.median()


 
df_out = pd.DataFrame(columns = column_names)


df_out.at[0,"stat"] = "std"
for c in column_names[1:]:
    df_out.loc[0,c] = med[c]


"""
med_l = list(med)
med_l.insert(0, "std")
df_out.loc[0, :] = med_l
"""

print(df_out.to_csv(index=False))