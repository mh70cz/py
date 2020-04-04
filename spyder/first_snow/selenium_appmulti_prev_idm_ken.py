#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27  2018 @author: mh70
"""

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pathlib import Path
import csv
import datetime
import os
import time
import sys


opts = Options()
opts.set_headless(False)


'''
When Page Loading takes too much time and you need to stop downloading 
additional subresources (images, css, js etc) you can change 
the  pageLoadStrategy through the webdriver.
'''
caps = DesiredCapabilities().FIREFOX
caps["pageLoadStrategy"] = "eager"  #  interactive
# caps["pageLoadStrategy"] = "normal"  #  complete
# caps["pageLoadStrategy"] = "none"   #  undefined
    
browser = Firefox(options=opts, capabilities=caps)
browser.implicitly_wait(2) # seconds
# An implicit wait tells WebDriver to poll the DOM 
# for a certain amount of time when trying to find 
# any element (or elements) not immediately available. 
# The default setting is 0. Once set, 
# the implicit wait is set for the life of the WebDriver object.


def get_password():
    home =  str(Path.home())
    pwd_file = home + '/Documents/local_info/selenium_appmulti_prev.txt'
    pwd_val = ''
    try:
        with open(pwd_file, "r", encoding = "utf8") as f:
            pwd_val = f.readline()
    except Exception as e:
        print(e)
        print('try insert password manually:')
        pwd_val = input("Password: ")
    return pwd_val


def gc_log_in(url, usr_val='cis.admin', pwd_val=''):
    if pwd_val == "":
        pwd_val = get_password()
    print('try to log in')        
    browser.get(url)
    usr = browser.find_element_by_id('Username')
    pwd = browser.find_element_by_id('Password')
    log_in = browser.find_element_by_class_name('btn-primary')
    usr.send_keys(usr_val)
    pwd.send_keys(pwd_val)
    log_in.click()
    
    try:
        ddtoggles = browser.find_elements_by_class_name('dropdown-toggle')
        for ddt in ddtoggles:
            # print('ddt: ' + str(ddt.text))
            if 'cis' in ddt.text and 'admin' in ddt.text:
                print("logged OK")
                return True
        print('not logged')
        return False
    except Exception as e:
        print(e)
        return False

init_url = 'http://appmultipreview/idmken'

subject_id = '14161673902'
strategy_type = 'Companies' #contains text
strategy_name = 'Atlas' #contains text

browser.get(init_url)
if 'sign-in' in browser.current_url:
    if gc_log_in(init_url):
        pass
    else:
        sys.exit('not able to log , exiting')


# url is remmaped by webserver e.g. https://cishd-mc-pre01.cis.local/.......        
current_url = browser.current_url 
url_pre = current_url[:current_url.rfind("/")]

browser.get(url_pre + '/NewQuery')
time.sleep(1)
#strategy type
links = browser.find_elements_by_tag_name('a')
for link in links:
    if strategy_type in link.text:
        link.click()
time.sleep(1)
#strategy name
elems = browser.find_elements_by_tag_name('td')
for e in elems:
    if strategy_name in e.text:
        e.click()

id = browser.find_element_by_id("Cb5SearchParameters.RegistrationNumber-1")
id.send_keys(subject_id)
consent = browser.find_element_by_id("Consent-1") # consent checkbox
if consent.is_selected() == False:
    consent.click()
browser.find_element_by_id("submit-query-btn").click()
time.sleep(1)
# open report
tds = browser.find_elements_by_tag_name("td")
for td in tds:
    if subject_id in td.text:
        td.click()
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
