#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mladík jsa tázán, jak je stár, odpověděl:
>Letos (1904) je mi právě tolik let, kolik činí ciferný součet roku mého narození<
Kolik let je mu?
"""

target_year = 1904


for year in range(1900, 1870, -1):
    age_y = target_year - year
    age_n = year // 1000 + (year % 1000)//100 + (year % 100) // 10 + year % 10
    if age_y == age_n: 
        print (f"birth year: {year},  num sum: {age_n} , age: {age_y} (already had a birthday)")
    
    #neodpovídá zadání jen pro info -- tento rok mi bude ...
    if age_y + 1 == age_n:
        print (f"birth year: {year},  num sum: {age_n} , age: {age_y } (will have a birthay)")
        
        
    