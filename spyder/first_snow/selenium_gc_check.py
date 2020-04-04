#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:31:25 2018 @author: mh70
"""

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pathlib import Path
import csv
import datetime
import os


opts = Options()
#opts.set_headless()
opts.headless = True
assert opts.headless # operation in headles mode


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



caches = {'GC290AN': 'Trapistický klášter',
          'GC40WZM': 'Pod mohutnym modrinem',
          'GC6QWNR': 'Polokacer',
          'GC6V72Y': 'Superkacer',
          'GC6ZNTB': 'Treti kacer',
          'GC7030Q': 'Kostel na Barrandove',
          'GC7JMAV': 'Kostel na Zlichove',          
          }

def get_password():
    home =  str(Path.home())
    pwd_file = home + '/Documents/pwd.txt'
    pwd_val = ''
    try:
        with open(pwd_file, "r", encoding = "utf8") as f:
            pwd_val = f.readline()
    except Exception as e:
        print(e)
        print('try insert password manually:')
        pwd_val = input("Password: ")
    return pwd_val


def gc_log_in(usr_val = 'mh70+ic76', pwd_val = ''):
    if pwd_val == "":
        pwd_val = get_password()
    print('try to log in')        
    browser.get('https://www.geocaching.com/account/login')
    usr = browser.find_element_by_id('Username')
    pwd = browser.find_element_by_id('Password')
    log_in = browser.find_element_by_id('Login')
    usr.send_keys(usr_val)
    pwd.send_keys(pwd_val)
    log_in.click()
    
    browser.get('https://www.geocaching.com/account/dashboard')
    try:
        logged_usr = browser.find_element_by_class_name('user-name')
        if logged_usr.text == 'mh70+ic76':
            print("logged OK")
            return True
    except Exception as e:
        print(e)
        return False
        
def save_to_file(fname, dict_to_save):
    with open(fname, 'w', newline='', encoding='utf-8') as csvfile:
        csv_out = csv.writer(csvfile)
        csv_out.writerow(["cache", "loggers"])

        # one value per row - rozvláčný zápis, jednodušší import
        for key, values in dict_to_save.items():
            for value in values:
                csv_out.writerow([key, value])  
        '''
        #- compact, but problems with import
        for key, values in dict_to_save.items():
            csv_out.writerow([key, values])
        '''
            

def read_from_file(fname):

    dict_to_import = dict()
    wrk_lst = list()
    with open(fname, 'r',  newline='', encoding='utf-8') as csvfile:
        csv_in = csv.reader(csvfile)
        next(csv_in) # header row
        for row in csv_in:
            t = tuple(row)
            wrk_lst.append(t)        

        caches = set([k[0] for k in wrk_lst])
        for cache in caches:
            wrk_sub_lst = list()
            for item in wrk_lst:
                if item[0] == cache:
                    wrk_sub_lst.append(item[1])
            dict_to_import[cache] = wrk_sub_lst
                
        return dict_to_import        
        
def get_caches_loggers():

    cache_loggers = dict()
    
    for cache in caches.keys():
        cache_url = 'https://coord.info/' + cache
        
        print (f'\n{cache} ({caches[cache]}):')
        browser.get(cache_url)
        logs_table = browser.find_element_by_id('cache_logs_table')
        loggers = logs_table.find_elements_by_class_name('logOwnerProfileName')
        loggers_lst = list()
        #print(str(cache) + ' ('+ caches[cache] +':')
        for l in loggers:
            print (l.text)
            loggers_lst.append(l.text)
        
        cache_loggers[cache] = loggers_lst
                
    now = datetime.datetime.today().strftime('%Y-%m-%dT%H%M%S')
    fname = './data/loggers' + now + '.txt'
    save_to_file(fname, cache_loggers)    
    

def compare(n=1):
    data_folder = './data'
    fnames = [fn for fn in os.listdir(data_folder) 
                if fn.endswith(".txt") and fn.startswith("loggers")  
             ]
    fnames.sort(reverse=True)
    
    if len(fnames) <= n :
        print('No data for comparison')
        return False
    print ('\n   *** Comparison ***')
    print(f'{fnames[0]} vs {fnames[n]}')
    
    last_dict = read_from_file('./data/' + fnames[0])
    refr_dict = read_from_file('./data/' + fnames[n])
    
    for cache in last_dict.keys():
        last = last_dict[cache]
        refr = refr_dict[cache]
        diff = [x for x in last if x not in refr]
        print(f'\n{cache} ({caches[cache]}):')
        print(diff)    

if gc_log_in():
    get_caches_loggers()
    compare(1)











'''
https://coord.info/GC290AN Trapistický klášter
https://coord.info/GC40WZM Pod mohutnym modrinem
https://coord.info/GC6QWNR Polokacer
https://coord.info/GC6V72Y Superkacer
https://coord.info/GC6ZNTB Treti kacer
https://coord.info/GC7030Q Kostel na Barrandove
https://coord.info/GC7JMAV Kostel naZlichove
'''


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
