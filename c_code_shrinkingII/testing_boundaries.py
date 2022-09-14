# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:18:24 2022

@author: gylmn
"""

import matplotlib.pyplot
import random

data = []
processed_data = []

# Fill with random data.
for i in range(0,99):
    datarow = []
    for j in range(0,99):
        datarow.append(random.randint(0,255))
    data.append(datarow)

print(data[-1][0])
print(data[0][99])
# Blur.
for i in range(0,99):
    datarow = []
    for j in range(0,99):
        print(i, j)
        print(i-1)
        sum1 = data[i][j]
        sum1 += data[i-1][j]
        sum1 += data[i+1][j]
        sum1 += data[i][j+1]
        sum1 += data[i][j-1]
        sum1 /= 5
    datarow.append(sum1)
    processed_data.append(datarow)

matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()
matplotlib.pyplot.imshow(processed_data)
matplotlib.pyplot.show()
