#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 22:10:47 2017

@author: mh70
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:07:57 2017

@author: mh70
"""

from collections import Counter
from collections import namedtuple

Word = namedtuple('Word', 'txt field link site area')

words = list()
dwords = list()
twords = list()

for item in big_list:
    
    link_text_lst = item[1].replace(",", "").replace(".", "").lower().split(" ")
    
        
    txt_lst = item[2].replace("  celý článek", "") \
                     .replace(",", "").replace("?", "").replace("!", "") \
                     .replace("\r","").replace("\n","").replace("\xa0","") \
                     .replace(".", "").lower().split(" ")
                     
    # remove empty words (result of multiple split char occurence)                 
    txt_lst = [x for x in txt_lst if x != "" ]                        
                         
    for word in txt_lst:
        w_txt = Word(word, 'text', item[0], item[3], item[4])
        words.append(w_txt)
        
    txt_lst_len = len(txt_lst)
      
    for i in range(0, txt_lst_len, 2):
        if (i + 1) < txt_lst_len:  
            dw_txt = Word(txt_lst[i] + " " + txt_lst[i + 1],
                          'text', item[0], item[3], item[4])
            dwords.append(dw_txt)
            if (i + 2) < txt_lst_len:  
                dw_txt = Word(txt_lst[i + 1 ] + " " + txt_lst[i + 2],
                              'text', item[0], item[3], item[4])
                dwords.append(dw_txt)
                
                
    for i in range(0, txt_lst_len, 3):
        if (i + 2) < txt_lst_len:  
            tw_txt = Word(txt_lst[i] + " "
                          + txt_lst[i + 1] + " " + txt_lst[i + 2],
                          'text', item[0], item[3], item[4])
            twords.append(tw_txt)
            if (i + 3) < txt_lst_len:  
                tw_txt = Word(txt_lst[i + 1 ] + " "
                              + txt_lst[i + 2] + " " + txt_lst[i + 3],
                              'text', item[0], item[3], item[4])
                twords.append(tw_txt)      
                if (i + 4) < txt_lst_len:  
                    tw_txt = Word(txt_lst[i + 2 ] + " "
                                  + txt_lst[i + 3] + " " + txt_lst[i + 4],
                                  'text', item[0], item[3], item[4])
                    twords.append(tw_txt)                   
    
   # words.extend(link_text_lst)
   # words.extend(txt_lst)  
    

most_words_200 = Counter(
        [word.txt for word in words 
         if len(word.txt) > 3 ]).most_common(200)


most_dwords_200 = Counter(
        [word.txt for word in dwords 
         if len(word.txt) > 3 ]).most_common(200)
    
most_twords_200 = Counter(
        [word.txt for word in twords 
         if len(word.txt) > 3 ]).most_common(200)      
    
    
most_words_ona_200 = Counter(
        [word.txt for word in words 
         if len(word.txt) > 3  and word.area == "ona"]).most_common(200)
    
    
most_dwords_ona_200 = Counter(
        [word.txt for word in dwords 
         if len(word.txt) > 3 and word.area == "ona"]).most_common(200)
    
most_twords_ona_200 = Counter(
        [word.txt for word in twords 
         if len(word.txt) > 3 and word.area == "ona"]).most_common(200)      
    

most_words_krimi_200 = Counter(
        [word.txt for word in words 
         if len(word.txt) > 3  and word.area == "krimi"]).most_common(200)
    
most_dwords_krimi_200 = Counter(
        [word.txt for word in dwords 
         if len(word.txt) > 3  and word.area == "krimi"]).most_common(200)

most_twords_krimi_200 = Counter(
        [word.txt for word in twords 
         if len(word.txt) > 3  and word.area == "krimi"]).most_common(200)    


most_words_biz_200 = Counter(
        [word.txt for word in words 
         if len(word.txt) > 3  and
         (word.area == "business" or word.area == "ekonomika") ]
        ).most_common(200)

"""  
most_words_200 = Counter(
        [word for word in words if len(word) > 3 ]).most_common(200)

dny_v_tydnu = [word for word in words if word in [
        "pondělí", "úterý", "středa", "středu", "čtvrtek", "pátek",
        "sobota", "sobotu",  "neděle", "neděli"
        ]]

dny_v_tydnu_7 = Counter(dny_v_tydnu).most_common(7)
"""


    

