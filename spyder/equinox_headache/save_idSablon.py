# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 12:58:00 2017

@author: mh70
"""
"""
ico = "N/A"

fname_sablony_id = "./sablony/sablony_id.txt"

with open(fname_sablony_id, 'a', encoding='utf-8') as outfile:
     for s_id in idSablon:
         outfile.write(str(s_id) + ", " + str(ico) + "\n")
         
"""
    
def append_id_sablon(idSablon, ico = "N/A"):
    fname_sablony_id = "./sablony/sablony_id.txt"
    
    with open(fname_sablony_id, 'a', encoding='utf-8') as outfile:
        for s_id in idSablon:
            outfile.write(str(s_id) + ", " + str(ico) + "\n")
            
            
append_id_sablon(idSablon, ico = "N/A")
