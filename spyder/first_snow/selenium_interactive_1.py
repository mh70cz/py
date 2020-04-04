#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http://selenium-python.readthedocs.io
https://realpython.com/blog/python/modern-web-automation-with-python-and-selenium/

dokumentace s příklady:
https://media.readthedocs.org/pdf/selenium-python/latest/selenium-python.pdf
    
"""

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless(False)
browser = Firefox(options=opts)
browser.get('https://www.ihned.cz')

x = browser.find_elements_by_class_name('article-title')
y = x[0].find_element_by_tag_name("a")
y.click()

browser.get_screenshot_as_file('./scrsht/img_1.png')

browser.set_window_size(800,2048)

browser.get_screenshot_as_file('./scrsht/img_2.png')

browser.minimize_window()
browser.maximize_window()

browser.back()
browser.refresh()



# scroll
browser.execute_script("window.scrollTo(0, 300)") 
y = 900
browser.execute_script("window.scrollTo(0, arguments[0])", y) 
#where y is the height, předání pomocí y -> arguments[0]

browser.set_window_size(300,600)
x, y = 150, 1200
browser.execute_script("window.scrollTo(arguments[0], arguments[1])", x, y) 

browser.set_window_size(600,600)
# scroll-down na konec okna
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")




#zavři cookie warning
cookies = browser.get_cookies()
cookies_old = cookies.copy()

#umožňuje zadat jen 1 class
cookie_warning_1 = browser.find_element_by_class_name('cc_btn_accept_all')

#umožňuje zadat více classes (.cc_btn and .cc_btn_accept_all)
cookie_warning_2 = browser.find_element_by_css_selector(
        '.cc_btn.cc_btn_accept_all')

cookie_warning_2.click() #clik for close warning banner

#najdi nově přidanou cookie
cookies = browser.get_cookies()
[c['name'] for c in cookies if c not in cookies_old]

browser.delete_cookie('cookieconsent_dismissed') 

