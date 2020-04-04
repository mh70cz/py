#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:07:57 2017

@author: mh70
"""

from collections import Counter


words = list()    
for item in big_list:
    
    link_text_lst = item[1].replace(",", "").replace(".", "").lower().split(" ")
    
    

    
    txt_lst = item[2].replace("  celý článek", "") \
                     .replace(",", "") \
                     .replace(".", "").lower().split(" ") 
    
    
    words.extend(link_text_lst)
    words.extend(txt_lst)
    
most_words_200 = Counter(
        [word for word in words if len(word) > 3 ]).most_common(200)

dny_v_tydnu = [word for word in words if word in [
        "pondělí", "úterý", "středa", "středu", "čtvrtek", "pátek",
        "sobota", "sobotu",  "neděle", "neděli"
        ]]

dny_v_tydnu_7 = Counter(dny_v_tydnu).most_common(7)



    

