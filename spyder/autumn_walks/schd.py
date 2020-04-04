#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 23:23:19 2018

@author: mh70
"""

"""

>>> import sched, time
>>> s = sched.scheduler(time.time, time.sleep)
>>> def print_time(a='default'):
...     print("From print_time", time.time(), a)
...
>>> def print_some_times():
...     print(time.time())
...     s.enter(10, 1, print_time)
...     s.enter(5, 2, print_time, argument=('positional',))
...     s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
...     s.run()
...     print(time.time())
"""
import sched, time

s = sched.scheduler(time.time, time.sleep)

def run_task():
    print("Ahoj")
    sched_task()
    
    
def sched_task():
    s.enter(2, 1, run_task)    
    print(s.queue)
    s.run()
    
sched_task()    