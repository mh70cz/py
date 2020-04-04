#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 23:02:08 2017

@author: mh70
"""

def my_decor(wrapped_func, num=15):
    def wrapper(text_to_print):
        if num <= 10:
            print(str(num) + " is less or equal than 10")
        else:
            print(str(num) + " is greater than 10")
        wrapped_func(text_to_print)
        print("after wrapped function is called")
    return wrapper

@my_decor
def test_func(text_to_print):
    print(text_to_print)
    
test_func("with @my_decor syntax sugar")   
#my_decor(test_func)("without wrapper syntax sugar")

    
#### based on http://scottlobdell.me/2015/04/decorators-arguments-python/
    
def pass_thru(func_to_decorate):
    def new_func(*original_args, **original_kwargs):
        print("function has been deforated")
        # do something here
        return func_to_decorate(*original_args, **original_kwargs)
    return new_func

@pass_thru
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3)
        
        
def print_args_without_decor_sytax_sugar(*args):
    for arg in args:
        print(arg)

pass_thru(print_args_without_decor_sytax_sugar)("alpha", "beta", "gamma")

##### Decorator with Arguments 
def decor_with_param(deco_arg1, deco_arg2):
    """ returns a function that will take a function to decorate """
    def real_decorator(func_to_decorate):
        def wrapper(*args, **kwargs):
            print("function which does something with %s and %s"
                  " has been decorated" % (deco_arg1, deco_arg2))
            func_to_decorate(*args, **kwargs)
        return wrapper
    return real_decorator

@decor_with_param("gin", "rum")
def print_args2(*args):
    for arg in args:
        print(arg)

print_args2(1, 2, 3)

def print_args2_without_decor_syntax_sugar(*args):
    for arg in args:
        print(arg)

decor_with_param("gin", "rum")(print_args2_without_decor_syntax_sugar)(1, 2, 3)

#### Class Based Decorator

class ClassBasedDecor(object):
    def __init__(self, func_to_decorate):
        print("INIT ClassBasedDecor")
        self.func_to_decorate = func_to_decorate
    def __call__(self, *args, **kwargs):
        print("CALL ClassBasedDecor")
        return self.func_to_decorate(*args, **kwargs)

@ClassBasedDecor
def print_more_args(*args):
    for arg in args:
        print(arg)

# init just once
print_more_args(1, 2, 3)
print_more_args(4, 5, 6)

def print_more_args_no_synt_sugar(*args):
    for arg in args:
        print(arg)

# inint for each call
ClassBasedDecor(print_more_args_no_synt_sugar)(1, 2, 3)
ClassBasedDecor(print_more_args_no_synt_sugar)(4, 5, 6)

