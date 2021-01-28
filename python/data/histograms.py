#!/usr/bin/env python3
# pip3 install matplotlib
# pip3 install numpy
import matplotlib.pyplot as plt
import numpy as np
import sys

file = sys.argv[1]

with open(file, 'rb') as io:
    x = np.load(io)
    # take a shape of (rows, columns)
    # and make 1 row and N columns appending each row's columns
    x_hist = np.squeeze(x.reshape(1,-1))
    plt.hist(x, bins=50)
    plt.show()
