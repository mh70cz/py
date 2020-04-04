#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 19:12:48 2018

@author: mh70
"""
import csv


pyd_lst = list()
qpy_lst = list()
spy_lst = list()

    
def read_from_file(fname):
    read_list = list()
    with open(fname, newline= '', encoding='utf-8') as csvfile:
        csv_in = csv.reader(csvfile)
        next(csv_in) #gets the first line
        for row in csv_in:
            t = tuple(row)
            read_list.append(t)
    return read_list

def fill_lists():
    
    fnames = ['pyd32018-02-11.csv', 'qpy32018-02-11.csv', 'spy2018-02-11.csv']
    read_list_names = ['pyd_lst', 'qpy_lst', 'spy_lst']
    
    for idx, fname in enumerate(fnames):
        lst = read_from_file(fname)
        print(len(lst))
        print(fname)
        globals()[read_list_names[idx]] = lst # write to global vars by name
        
fill_lists()    

p = pyd_lst
q = qpy_lst
s = spy_lst 

# [[x for x in a if a not in b], [x for x in b if x not in a]]

    
#([x for x in a if x not in b], [x for x in b if x not in a])

[
len([x for x in p if x not in q]),
len([x for x in p if x not in s]),

len([x for x in q if x not in p]),
len([x for x in q if x not in s]),

len([x for x in s if x not in p]),
len([x for x in s if x not in q])
]

pq = [x for x in p if x not in q]
ps = [x for x in p if x not in s]
qs = [x for x in q if x not in s]

len([ x for x in pq if x not in ps])
len([ x for x in ps if x not in qs])
len([ x for x in pq if x not in qs])

len([x for x in ps if x in q])
len([x for x in p if( x not in q) or (x not in s)])

