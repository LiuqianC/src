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

#Functions
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
    #print("distance between [", x0, y0, "] and [", x1, y1, "] =", distance)
    return distance

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
    #min_distance = math.inf
    for i in range(len(agents)):
        a = agents[i] #a is a list
        for j in range(i+1, len(agents)):
            b = agents[j] #b is a list
            distance = get_distance(a[0], a[1], b[0], b[1]) #a[0] is a number
            #print("i", i, "j", j)
            max_distance = max(max_distance, distance)
            #min_distance = min(min_distance, distance)
    print("max_distance", max_distance)
    #print("min_distance", min_distance)
    return max_distance#, min_distance

#Main
# Set the pseudo-random seed for reproducibility
random.seed(0)

# Initialise agents
agents = []
# Create a times list to store time value
times = []
# Create a number list to store the number of agents
numbers= []
#Variables for constraining movement
n_iterations = 1000
#The minimum x coordinate
x_min = 0
#The minimum y coordinate
y_min = 0
#The maximum x coordinate
x_max = 99
#The maximum y coordinate
y_max = 99

# Change n_gents in range 500 to 4500
for n_agents in range(500, 5000, 500): #500,1000,1500
    agents=[]
    numbers.append(n_agents)
    for i in range(n_agents):
        agents.append([random.randint(0, 99), random.randint(0, 99)])
    #record the start time 
    start = time.perf_counter()
    #Start to get distance and the max distance
    get_max_distance(agents)
    #reord the end time
    end = time.perf_counter()
    run_time = end - start
    print("Time taken to calculate maximum distance", run_time, "seconds")
    times.append(run_time)

#Create a list to store dots coordinates pairs
dots = [] #dots[x][y], x=number of agents, y=times

#Store the dots coordinates
for i in range(len(numbers)):
    dots.append([numbers[i], times[i]])

#Plot
plt.title("Time taken to calculate maximum distance for different numbers of agents")
plt.xlabel("Numbers of agnets")
plt.ylabel("Time")
for i in range(len(dots)):
    plt.scatter(dots[i][0],dots[i][1],color='black')
plt.show()

#%%Movement
for loop in range(n_iterations):
    # Change agents[i] coordinates randomly
    #x-coordinate
    for i in range(n_agents):
        rn = random.random()
        if rn <0.5:
            agents[i][0]+=1
        else:
            agents[i][0]-=1
        #y-coordinate
        rn = random.random()
        if rn<0.5:
            agents[i][1]+=1
        else:
            agents[i][1]-=1
        #Apply movement constraints
        if agents[i][0]<x_min:
            agents[i][0]=x_min
        if agents[i][1]<y_min:
            agents[i][1]=y_min
        if agents[i][0]>x_max:
            agents[i][0]=x_max
        if agents[i][1]>y_max:
            agents[i][1]=y_max



        