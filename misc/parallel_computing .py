# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 18:15:28 2017

@author: mh70
"""

import collections
import multiprocessing

def f(x):
    return x*x


Scientist = collections.namedtuple('Scientist', [
    'name',
    #'field',
    'born'
    ])

scientists = (
    Scientist(name='Ada Lovelace', born=1815),
    Scientist(name='Emmy Noether', born=1882),
    Scientist(name='Marie Curie', born=1867),
    Scientist(name='Tu Youyou', born=1930),
    Scientist(name='Ada Yonath', born=1939),
    Scientist(name='Vera Rubin', born=1928),
    Scientist(name='Sally Ride', born=1951),
    )

def process_item(item):
    return {
        'name': item.name,
        'age': 2017 - item.born
        }

if __name__ == '__main__': # bez tohoto řádku to zakousne konsoli
    pool = multiprocessing.Pool()
    result = pool.map(process_item, scientists)
    print(tuple(result))
