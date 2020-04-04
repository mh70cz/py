#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 22:24:06 2017

@author: mh70
"""

import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.path import Path
import math

fig, ax = plt.subplots()
ax.set_aspect('equal')
# plt.axis('off')

center = (0.0, 0.0)
radius = 0.9
radius_inner = 0.8
radius_outer = 1.1

n_cogs = 13
cog_ang_width_inner = 12 
cog_ang_width_outer = 6

ts = [x*(360/n_cogs) for x in range(n_cogs)]

centre_cogs = []

for t in ts:
    x = radius * math.cos(math.radians(t))
    y = radius * math.sin(math.radians(t))
    centre_cogs.append((x, y))
    
    
def circular(ts):
    while True:
        for t in ts:
            yield t
tc = circular(ts)


t = next(tc)
for idx in ts:    
    th1_inner = t + cog_ang_width_inner/2
    th1_outer = t - cog_ang_width_outer/2
    th2_outer = t + cog_ang_width_outer/2
    
    alpha = (radius_inner * math.cos(math.radians(t - cog_ang_width_inner/2)),
             radius_inner * math.sin(math.radians(t - cog_ang_width_inner/2)))
    
    beta = (radius_outer * math.cos(math.radians(t - cog_ang_width_outer/2)),
            radius_outer* math.sin(math.radians(t - cog_ang_width_outer/2)))
    
    gamma = (radius_outer * math.cos(math.radians(t + cog_ang_width_outer/2)),
             radius_outer * math.sin(math.radians(t + cog_ang_width_outer/2)))

    delta = (radius_inner * math.cos(math.radians(t + cog_ang_width_inner/2)),
             radius_inner * math.sin(math.radians(t + cog_ang_width_inner/2)))    
    
    t = next(tc)
    th2_inner = t - cog_ang_width_inner/2
    a_inner = patches.Arc(center, (radius - 0.1)  * 2, (radius - 0.1) * 2,
                          angle=0, theta1=th1_inner, theta2=th2_inner,
                          color = "green")
    a_outer= patches.Arc(center, (radius_outer)  * 2,
                         (radius_outer) * 2,
                      angle=0, theta1=th1_outer, theta2=th2_outer,
                      color = "green")
    ax.add_patch(a_inner)
    ax.add_patch(a_outer)
    
#    for p in [alpha, beta, gamma, delta]:
#        ax.plot(p[0], p[1], "o", color="b")
    ax.plot([alpha[0], beta[0]], [alpha[1], beta[1]], color="green")
    ax.plot([gamma[0], delta[0]], [gamma[1], delta[1]], color="green")
        


#ax.plot([x[0] for x in  centre_cogs],
#        [y[1] for y in  centre_cogs],
#        "o", color="r")

# plt.savefig("test.svg")