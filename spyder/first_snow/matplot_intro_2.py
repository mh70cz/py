#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://realpython.com/blog/python/python-matplotlib-guide/
"""
from io import BytesIO
import tarfile
from urllib.request import urlopen
import matplotlib.pyplot as plt
import numpy as np

url = 'http://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.tgz'
b = BytesIO(urlopen(url).read())
fpath = 'CaliforniaHousing/cal_housing.data'

with tarfile.open(mode='r', fileobj=b) as archive:
    housing = np.loadtxt(archive.extractfile(fpath), delimiter=',' )
    
y = housing[:, -1] # area's average home value
pop, age = housing[:, [4, 7]].T # area's population , average house age

def add_titlebox(ax, text):
    ax.text(.55, .8, text, 
            horizontalalignment='center',
            transform = ax.transAxes,
            bbox=dict(facecolor='white', alpha=0.6),
            fontsize=12.5)
    return ax

gridsize = (3, 2)
fig = plt.figure(figsize=(12, 8))
ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
ax2 = plt.subplot2grid(gridsize, (2, 0))
ax3 = plt.subplot2grid(gridsize, (2, 1))

ax1.set_title('Home value as a function of home age & area population', 
              fontsize=14)
sctr = ax1.scatter(x=age, y=pop, c=y, cmap='RdYlGn')
plt.colorbar(sctr, ax=ax1, format='$%d')
ax1.set_yscale('log')
ax2.hist(age, bins='auto')
ax3.hist(pop, bins='auto', log=True)

add_titlebox(ax2, 'Historogram: home age')
add_titlebox(ax3, 'Historogram: area population  (log scl.)')

# ***********

fig1, ax1 = plt.subplots()
id(fig1)
id(plt.gcf())

fig2, ax2 = plt.subplots()
id(fig2)
id(plt.gcf())
# ******

x = np.diag(np.arange(2,12))[::-1]
x[np.diag_indices_from(x[::-1])] = np.arange(2, 12)
x2 = np.arange(x.size).reshape(x.shape)