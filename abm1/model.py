# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 00:03:27 2023

@author: ASUS
"""
#import package
import random
import math

# Initialise variable x0
x0 =0
print ("x0",x0)

# Initialise variable y0
y0 =0
print("y0",y0)

#Set the pseudo-random seed for reproducibility
random.seed(0)#each seed number has a unique random number

# Change x0 and y0 randomly
rn = random.random()#if the seed is determined, the random number is determined, otherwise the random numbers are differnt every times
print(rn)

# =============================================================================
# #Using if-else loop
# b = rn<0.5 # b is a bool value. True or False
# print("b",b)
# if b: # if b is True
#     x0 = x0 + 1 # x0's value +1
# else: #if b is false
#     x0 = x0 - 1 #x0's value -1
# print ("x0",x0)
# =============================================================================

# Using if-else loop
if rn < 0.5: # rn<0.5 is true
    x0 = x0 + 1
else: #rn>0.5
    x0 = x0 - 1
print ("x0",x0)

# Initialise variable x1
x1 = 0

# Initialise variable y1
y1 = 0

# Change x1 and y1 randomly
x1 = random.randint(0, 99) # get x1 a value from 0 to 99
y1 = random.randint(0, 99) # get y1 a value from 0 to 99

# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Initialise x0, y0, x1, y1
x0 = 0
y0 = 0
x1 = 3
y1 = 4
# Calculate the difference in the x coordinates.
a = x1 - x0
# Calculate the difference in the y coordinates.
b = y1 - y0
# Square the differences and add the squares
c = a**2 + b**2
# Calculate the square root
dist = math.sqrt(c)
print ("The Euclidean distance between (x0, y0) and (x1, y1) = ", dist)
