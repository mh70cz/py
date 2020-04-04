#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 19:54:43 2018

@author: mh70
"""

import numpy

array1 = numpy.array([1, 2, 3, 4, 5, 6])

array2 = numpy.array([[1, 2, 3],[4, 5, 6]])

print(array2.shape)
array2[0,:]
array2[:,0]
array2[1,:] = 0
array2[:,2] = -1


array1[1:3]
array1[1:3] = [-2, -3]
array1[::2]
array1[:3]
array1[3:]
array1[-3:]

ar3 = numpy.array([[n+m*5 for n in range(10)] for m in range(10)]) 

ar3[1:4, 2:5]
ar3[1:4, :]
ar3[::2, ::2 ]

B = numpy.array([[n+m*5 for n in range(4)] for m in range(4)])
numpy.dot(B, B)

B*B
A = B.T
A*B
A*B == B * B.T

C = numpy.array([[1, 2, 3], [4, 5, 6], [-7, 8, 9]])
numpy.linalg.inv(C)
numpy.linalg.det(C)

numpy.shape(B)
numpy.mean(B[:,3])
numpy.sum(B)
numpy.mean(B)

numpy.std(B[:,3])

numpy.var(B[:,3])

D = numpy.arange(0, 20, 2)
numpy.sum(D)
numpy.prod(D+1)
numpy.cumsum(D)
numpy.cumprod(D+1)
numpy.diag(B).sum()
