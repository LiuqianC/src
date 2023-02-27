# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:17:45 2023

@author: ASUS
"""

import random
import math
import matplotlib
from matplotlib import pyplot as plt
import operator
import time
import agentframework as af

#Define a function to calculate the distance
def get_distance(x0, y0, x1, y1):
    '''
    Calculate the Euclidean distance between (x0, y0) and (x1, y1).

    Parameters
    ----------
    x0 : Number
        The x-coordinate of the first coordinate pair.
    y0 : Number
        The y-coordinate of the first coordinate pair.
    x1 : Number
        The x-coordinate of the second coordinate pair.
    y1 : Number
        The y-coordinate of the second coordinate pair.

    Returns
    -------
    distance : Number
        The Euclidean distance between (x0, y0) and (x1, y1).

    '''
    distance = math.sqrt((x0-x1)**2+(y0-y1)**2)
    print("distance between [", x0, y0, "] and [", x1, y1, "] =", distance)
    return distance
   #print("distance=", distance)

#Define a function to calcuate the max distance
def get_max_distance(agents):
    '''
    Calculate the max distance among these points
    
    Parameters
    ----------
    agents: list
        The list which contains ten dots coordinate pair

    Returns
    -------
    max_distance: Number
        The max distance between two farest points

    '''
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i] #a is a list
        for j in range(len(agents)):
            b = agents[j] #b is a list
            distance = get_distance(a.x, a.y, b.x, b.y) #a[0] is a number
            max_distance = max(max_distance, distance)
    print("max_distance", max_distance)
    return max_distance

# Set the pseudo-random seed for reproducibility
random.seed(0)

# A variable to store the number of agents
n_agents = 10

# A variable to store the number of iterations
n_iterations = 10
# # Initialise Agent a
# a = af.Agent()
#'''
# agentframework.py

# import random

# class Agent():
#     def __init__(self):
#         self.x = random.randint(0, 99)
#         self.y = random.randint(0, 99)
    
#     def __str__(self):
#         return self.__class__.__name__ + "(x=" + str(self.x)\
#             + ", y=" + str(self.y) + ")"
# '''
# print("type(a)",type(a))
# print(a)

# Initialise agents
agents = []
for i in range(n_agents):
    #Create an agent
    agents.append(af.Agent(i))
    #print(agents[i])
print(agents)

# Move agents
# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99
# Movement
for loop in range(n_iterations):
    for i in range(len(agents)):
        agents[i].move(x_min, y_min, x_max, y_max)

# # Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# # Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4
# x0 = 0
# y0 = 0
# x1 = 3
# y1 = 4
# get_distance(x0, y0, x1, y1) #Use the function

# Plot
for i in range(n_agents):
    plt.scatter(agents[i].x, agents[i].y, color='black')
# Plot the coordinate with the largest x red
# use operator.itemgetter(0/1) when using list
# use operator.attrgetter(x/y) when using class
lx = max(agents, key=operator.attrgetter('x'))
plt.scatter(lx.x, lx.y, color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.attrgetter('x'))
plt.scatter(sx.x, sx.y, color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.attrgetter('y'))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.attrgetter('y'))
plt.scatter(sy.x, sy.y, color='green')
plt.show()

#record the start time 
start = time.perf_counter()

#Start to get distance and the max distance
get_max_distance(agents)

#reord the end time
end = time.perf_counter()
print("Time taken to calculate maximum distance", end - start, "seconds")


