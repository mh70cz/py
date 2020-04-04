"""
xl.parse(1, parse_cols=[0], skiprows=[0], names=["Country"])
xl.parse(1, parse_cols=[0], skiprows=[1], names=["Country"])
"""

from pathlib import Path
import pandas as pd


home = str(Path.home())
file = home + "/Downloads/battledeath.xlsx"
xl = pd.ExcelFile(file)

no_skip_row = xl.parse(1, parse_cols=[0], names=["Country"])
skip_row_0 = xl.parse(1, parse_cols=[0], skiprows=[0], names=["Country"])
skip_row_1 = xl.parse(1, parse_cols=[0], skiprows=[1], names=["Country"])

print("no skip row:")
print(no_skip_row.head())
print("skip row 0:")
print(skip_row_0.head())
print("skip row 1:")
print(skip_row_1.head())
print("skip_row_0 and skip_row_1 give the same result - strange:")
print(skip_row_0.head() == skip_row_1.head())
