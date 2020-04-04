# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:04:39 2018

@author: mh70
"""

from timeit import timeit


def in_test(iterable):
    for i in range(1000):
        if i in iterable:
            pass



# from __main__ import
timeit('in_test(iterable)',
       setup="from __main__ import in_test;  iterable = list(range(1000))",
       number=1000) #list

timeit('in_test(iterable)',
       setup="from __main__ import in_test;  iterable = set(range(1000))",
       number=1000) #set


# globals=globals() define in setup
timeit("in_test(iterable)" ,
       setup = "iterable = list(range(1000))",
       globals=globals(),
       number=1000
       ) #list

timeit("in_test(iterable)" ,
       setup = "iterable = set(range(1000))",
       globals=globals(),
       number=1000
       ) #set

# globals=globals() define outside
ITER_L = list(range(1000))
ITER_S = set(range(1000))

timeit("in_test(ITER_L)" ,
       globals=globals(),
       number=1000
       ) #list

timeit("in_test(ITER_S)" ,
       globals=globals(),
       number=1000
       ) #set




def no_duplicates(list):
    no_duplicate_list = []
    [no_duplicate_list.append(item) for item in list if item not in no_duplicate_list]
    return no_duplicate_list
# first, let's see how the list perform:
timeit('no_duplicates([1, 2, 3, 1, 7])', 
       globals=globals(), 
       number=1000)

timeit('list(set([1, 2, 3, 1, 2, 3, 4]))', 
       number=1000)

