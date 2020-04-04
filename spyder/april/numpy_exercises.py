# -*- coding: utf-8 -*-

"""
https://www.machinelearningplus.com/python/101-numpy-exercises-python/
101 NumPy Exercises for Data Analysis (Python)
"""

import numpy as np

def np_version():
    """ 1. print the version number """
    return np.__version__


def np_02_03():
    """
    2. create a 1D array of numbers from 0 to 9
    desired output: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    
    a = np.arange(10)
    print(a)


    """    
    3. create and 3 x 3 numpy array of all True's
    """    
    x = np.full((3,3), True, dtype=bool)
    y = np.ones((3,3), dtype=bool)
    assert(x.all() == y.all())    
    print(x)
    
