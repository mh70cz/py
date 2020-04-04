# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 07:31:29 2017

@author: mh70
"""
import time

class MyBusinessException(Exception):
    pass

def wrt_f(label = "", msg="", header = False):
    fname = './x/GEO_Cb4_rqu+rsp.txt'
#    header = True
#    msg = "msg"
#    label = "lgl"
    
    now_str = time.strftime("%c")
    
    if header:
        with open(fname, 'w') as file:
            file.write(now_str + '   GEO_Cb4 requests and responses -- ' +  '\n')
    
    if label != "" or msg != "":
        with open(fname, 'a', encoding='utf-8') as file:
            if label != "":
                file.write(now_str + '   ' + label + '\n\n')
            if msg != "":
                file.write(msg)
            file.write('\n====================================================\n\n')
            