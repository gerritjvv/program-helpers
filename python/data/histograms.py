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

    print(f"SHAPE: {x_hist.shape}")

    bins = 100

    plot1 = plt.figure(1)
    # histogram
    plt.hist(x_hist, bins=bins)
    # normalised histogram
    plt.figure(2)
    plt.hist(x_hist, bins=bins, density=1, weights=np.ones_like(x_hist)/x_hist.shape[0])

    plt.show()
