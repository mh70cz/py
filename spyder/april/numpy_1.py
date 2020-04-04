# -*- coding: utf-8 -*-

import numpy  as np
import matplotlib.pyplot as plt

np.random.seed(444)

N = 10000

sigma = 0.1

noise = sigma * np.random.randn(N)
x = np.linspace(0, 2, N)

d = 3 + 2 * x + noise
d.shape = (N, 1)


X = np.column_stack((np.ones(N, dtype=x.dtype), x))

"""
fig, ax = plt.subplots()
ax.plot(noise)
ax.legend(loc='upper left')
plt.show()
"""

fig, ax = plt.subplots()
ax.plot(x, label="x")
ax.plot(d, label="d")

ax.legend(loc='upper left')
plt.show()


