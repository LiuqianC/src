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
            distance = get_distance(a[0], a[1], b[0], b[1]) #a[0] is a number
            max_distance = max(max_distance, distance)
    print("max_distance", max_distance)
    return max_distance

# Set the pseudo-random seed for reproducibility
random.seed(0)

# A variable to store the number of agents
n_agents = 10

# Initialise agents
agents = []
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
print(agents)

# Move agents
for i in range(n_agents):
    # Change agents[i] coordinates randomly
    # x-coordinate
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    # y-coordinate
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1
print(agents)

# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4
x0 = 0
y0 = 0
x1 = 3
y1 = 4
get_distance(x0, y0, x1, y1) #Use the function

# Plot
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
# Plot the coordinate with the largest x red
lx = max(agents, key=operator.itemgetter(0))
plt.scatter(lx[0], lx[1], color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.itemgetter(0))
plt.scatter(sx[0], sx[1], color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.itemgetter(1))
plt.scatter(ly[0], ly[1], color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.itemgetter(1))
plt.scatter(sy[0], sy[1], color='green')
plt.show()


#record the start time 
start = time.perf_counter()

#Start to get distance and the max distance
get_max_distance(agents)

#reord the end time
end = time.perf_counter()
print("Time taken to calculate maximum distance", end - start, "seconds")


