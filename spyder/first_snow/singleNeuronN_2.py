#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 14:10:12 2018

@author: mh70
"""

from numpy import exp, array, random, dot
import unittest

class neural_network:
    def __init__(self):
        random.seed(1)
        self.weights = 2 * random.random((3,1)) - 1
    
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))
    
    def train(self, inputs, outputs, num):
        for iteration in range(num):
            nn_out = self.think(inputs)
            error = outputs - nn_out
            adjustment = dot(inputs.T , error * nn_out * (1 - nn_out))
            self.weights += adjustment
            
    def think (self, inputs):
        result = self.__sigmoid(dot(inputs, self.weights))
        return result
    
network = neural_network()    

inputs = array([[1, 1, 1],
                [1, 0, 1],
                [0, 1, 1],
                ])
outputs = array([[1, 1, 0]]).T

network.train(inputs, outputs, 10_000)

print (network.think(array([1, 0, 0])))


class TestNn(unittest.TestCase):
    """ test basic functionality """
    
    tst_in = [[1, 1, 0],
              [1, 0, 1],
              [1, 1, 1],
              [0, 1, 0],
              [0, 1, 1],
              ]
    tst_out = [1, 1, 1, 0, 0,]
    
    def test_a(self):
        for idx, inp in enumerate(self.tst_in):
            nn_out = network.think(inp)[0]
            self.assertAlmostEqual(nn_out, self.tst_out[idx], 
                                   delta = 0.1, msg= str(idx))
    def test_exception(self):
        nn_out = network.think([0, 0, 0])
        # for [0, 0, 0] dot method returns 0 -> __sigmoid returns 0.5 
        self.assertEqual(nn_out[0], 0.5)

unittest.main()            