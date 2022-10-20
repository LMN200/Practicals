# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:12:28 2022

@author: gylmn
"""

# Make a y variable
# Make a x variable
# Change y and x based on random numbers
# Make a second set of y and x, and make these chnage randomly as well
# Work out the distance between the two sets of y and x




y0 = 50
x0 = 50

print (y0)

import random

if random.random() < 0.5:
    y0 = y0 + 1
else:
        y0 = y0 - 1

if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
    
print (y0, x0)




y1 = 50
x1 = 50


if random.random() < 0.5:
    y1 = y1 + 1
else:
        y1 = y1 - 1

if random.random() < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
    
print (y1, x1)



#y01 = 50
#x01 = 50 


#if random.random() < 0.5:
#    y01 += 1
#else:
#    y01 -= 1
    
#if random.random() < 0.5: 
#    x01 += 1
#else:
#    x01 -= 1
    
#print (y01, x01)
    
#y0 = 0
#x0 = 0
#y1 = 4
#x1 = 3

    
y_diff = (y0 - y1) 
y_diffsq = y_diff * y_diff

x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff

sum = y_diffsq + x_diffsq

answer = sum**0.5

print(answer)   
    

import random

agents = []

agents.append([y0, x0])
    
    
    
    
    
    
    
    
    
    
    
    
    