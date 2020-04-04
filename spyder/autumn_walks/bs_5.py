#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:55:09 2017

@author: mh70
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
#from collections import Counter 



sources_to_parse = [
    ("http://lidovky.cz", "lidovky.cz", "title"),
    ("http://byznys.lidovky.cz", "lidovky.cz", "business"),
    ("http://www.lidovky.cz/zpravy-svet.aspx", "lidovky.cz", "svet"),
    ("http://www.lidovky.cz/zpravy-domov.aspx", "lidovky.cz", "domov"),
    ("https://sport.lidovky.cz/", "lidovky.cz", "sport"),
    ("https://www.lidovky.cz/kultura.aspx", "lidovky.cz", "kultura"),
    ("https://cestovani.lidovky.cz/", "lidovky.cz", "cestovani"),
    ("https://relax.lidovky.cz/", "lidovky.cz", "relax"),
    ("https://www.lidovky.cz/design.aspx", "lidovky.cz", "design"),
    ("https://www.lidovky.cz/dobra-chut.aspx", "lidovky.cz", "chut"),
    ("https://www.lidovky.cz/nazory.aspx", "lidovky.cz", "nazory"),
    ("https://www.lidovky.cz/lide.aspx", "lidovky.cz", "lide"),
    ("https://www.lidovky.cz/video.aspx", "lidovky.cz", "video"),
    ("https://www.lidovky.cz/specialy.aspx", "lidovky.cz", "specialy"),
    ("http://www.idnes.cz/", "idnes.cz", "title"),
    ("http://zpravy.idnes.cz/", "idnes.cz", "zpravy"),
    ("http://zpravy.idnes.cz/krimi.aspx", "idnes.cz", "krimi"),
    ("https://kultura.zpravy.idnes.cz/", "idnes.cz", "kultura"),
    ("https://ekonomika.idnes.cz/", "idnes.cz", "ekonomika"),
    ("https://bydleni.idnes.cz/", "idnes.cz", "bydleni"),
    ("https://ona.idnes.cz/", "idnes.cz", "ona"),
    ("https://revue.idnes.cz/", "idnes.cz", "revue"),
    ("https://auto.idnes.cz/", "idnes.cz", "auto"),
                   ]

"""
my_url = "https://www.lidovky.cz/dobra-chut.aspx"
site = "lidovky.cz"
area = "chut"
"""


def source_soup(my_url):
    uClient = uReq(my_url)
    page_html = uClient.read()
    return soup(page_html, "html.parser")


def parse_perex_alone(page_soup, parsed_info, site, area):
    p_perex_lst = [x for x in page_soup.find_all("p", {"class": "perex"})]
    for p_perex in p_perex_lst:
        parent = p_perex.parent
        a_lst = parent.find_all("a")
        try:
            link = a_lst[0].attrs["href"]
        except:
            link = None
        try:
            link_text = a_lst[0].text.strip()
        except:
            link_text = None
        try:
            txt = p_perex.text.strip()
        except:
            txt = None
        parsed_info.append((link, link_text, txt, site, area))


    p_alone_lst = [x for x in page_soup.find_all("p", {"class": "alone"})]
    for p_alone in p_alone_lst:
        link = p_alone.a.attrs["href"]
        link_text = p_alone.a.text.strip()
        txt = p_alone.text.strip()
        if link_text.strip() == txt:
            txt = ""
        parsed_info.append((link, link_text, txt, site, area))

    return parsed_info

def parse():
    parsed_info_coll = list()
    for s in sources_to_parse:
        my_url, site, area = s
        print(my_url)
        parsed_info = list()
        page_soup = source_soup(my_url)
        parsed_info = parse_perex_alone(page_soup, parsed_info, site, area) # 2017-10-23 WTF parse_info? 
        parsed_info_coll.extend(parsed_info)
    return parsed_info_coll
