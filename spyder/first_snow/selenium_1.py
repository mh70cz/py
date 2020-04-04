#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:31:25 2018

@author: mh70
"""

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.set_headless()
assert opts.headless # operation in headles mode
browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')

search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('real python')
search_form.submit()

results = browser.find_elements_by_class_name('result')

print(results[0].text)


browser.close()


opts = Options()
opts.set_headless()
browser = Firefox(options=opts)
browser.get('https://bandcamp.com')
browser.find_element_by_class_name('playbutton').click()

tracks = browser.find_element_by_class_name('discover-item')
len(tracks)
tracks[3].click()