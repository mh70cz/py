# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Wed Jul  3 14:48:20 2019 
"""

import os
from bs4 import BeautifulSoup as soup


"""

"""
src_dir = r"c:\temp"
src_file = r"Changes_after_Go_Live.txt"
src_path = os.path.join(src_dir, src_file)

with open(src_path) as reader:
    div_html = reader.read()
    
div_soup = soup(div_html, "html.parser")

tickets = div_soup.find_all("div", {"class": "la-primary-data-id"})


id_list = []

for ticket in tickets:
    id_ = ticket.text    
    par_ticket = ticket.find_parent()
    long_desc = par_ticket.text
    a = par_ticket.find("a").attrs["href"]
    
    desc = long_desc.split("|")[-1].strip()
    id_list.append(int(id_))
    
    print(f"{id_}; https://cisvsts.visualstudio.com{a}; {desc}")

