#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 14:20:53 2018

@author: mh70
"""

from numpy  import exp, array, random, dot
import matplotlib.pyplot as plt
import unittest

class neural_network:
    def __init__(self):
        random.seed(1)
        self.weights = 2 * random.random((2, 1)) -1
        
        
    def train(self, inputs, outputs, num):
        for iteration in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = 0.01 * dot(inputs.T, error)
            self.weights += adjustment
            
    def think(self, inputs):
        return (dot(inputs, self.weights))
    
neural_network = neural_network()    

#the training set
inputs = array([[2, 3], [1, 1], [5, 2], [12, 3]])

outputs = array([[10, 4, 14, 30]]).T

neural_network.train(inputs, outputs, 100)

# print(neural_network.think(array([15, 2])))

# print(neural_network.think(array([91, 17])))
diff_arr = []
n = 900
rint1 = random.randint(1, 9999, n)
rint2 = random.randint(1, 9999, n)

for i in range(n):
    out = 2 * (rint1[i] + rint2[i])
    nn_out = neural_network.think(array([rint1[i], rint2[i]]))
    nn_out = nn_out[0]
    diff = abs(out - nn_out)/(rint1[i] + rint2[i])
    
    diff_arr.append([rint1[i], rint2[i], diff])

x = [ e[0] for e in  diff_arr]
y = [ e[1] for e in  diff_arr]
z = [ e[2]*10000 for e in  diff_arr]
fig, ax = plt.subplots()
ax.scatter(x, y, c=z)
plt.show()



class TestNn(unittest.TestCase):
    """ test basic functionality """
        
    tst_lst = list()
    n = 50
    rint1 = random.randint(1, 9999, n)
    rint2 = random.randint(1, 9999, n)

    for i in range(n):
        tst_lst.append([rint1[i], rint2[i], 2 * (rint1[i] + rint2[i])])
    
    def test_tst_lst(self):
        for i in range(self.n):
            x = self.tst_lst[i]
            self.assertEqual(2 * (x[0] + x[1]), x[2])
            
    def test_nn(self):
        for i in self.tst_lst:
            nn_out = neural_network.think(array([i[0], i[1]]))
            self.assertEqual(int(round(nn_out[0], 2)) ,i[2])            

# unittest.main()         
            