#!/usr/bin/env python3
# pip3 install scipi
# pip3 install matplotlib

# see: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

data = [4.96, 4.98, 5.02, 5.04]

for x in data:
    # loc == mean, scale == standard deviation
    print(scipy.stats.norm.pdf(x, loc=5, scale=0.02))


fig, ax = plt.subplots(1, 1)

x = np.linspace(scipy.stats.norm.ppf(0.01),
                scipy.stats.norm.ppf(0.99), 100)

ax.plot(x, scipy.stats.norm.pdf(x),
       'r-', lw=5, alpha=0.6, label='norm pdf')

ax.hist(data, density=True, histtype='stepfilled', alpha=0.2)

plt.show()