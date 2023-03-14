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
import my_modules.io as io
import my_modules.agentframework as af
import csv
import my_modules.geometry as gm
import imageio
import os

#%%FUNCTIONS
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
            distance = gm.get_distance(a.x, a.y, b.x, b.y) #a[0] is a number
            max_distance = max(max_distance, distance)
    #print("max_distance", max_distance)
    return max_distance

def addup_environment(environment):
    sum_env = 0
    for i in range(len(environment)):
        for j in range(len(environment[i])):
            sum_env += environment[i][j]
    return sum_env

def addup_store(agents):
    sum_store = 0
    for i in range(len(agents)):
        sum_store += agents[i].store
    return sum_store

def write_in(environment):
    f = open('../../data/output/out.txt','w', newline='')
    writer = csv.writer(f)
    for row in environment:
        writer.writerow(row) #list of values
    f.close()

if __name__ == '__main__':
    #%%INPUT
    n_rows,n_cols,environment=io.read_data()

    #%%VARIABLES INITIALISE
    # Set the pseudo-random seed for reproducibility
    random.seed(0)

    # A variable to store the number of agents
    n_agents = 10

    # A variable to store the number of iterations
    n_iterations = 10

    # Variables for constraining movement.
    # The minimum x coordinate.
    x_min = 0
    # The minimum y coordinate.
    y_min = 0
    # The maximum an agents x coordinate is allowed to be.
    x_max = n_cols - 1
    # The maximum an agents y coordinate is allowed to be.
    #y_max = 99
    y_max = n_rows - 1

    # print("type(a)",type(a))
    # print(a)
    # A variable to store the constraint of neighbours
    neighbourhood = 50

    #%%AGENTS INITIALISE
    # Initialise agents
    agents = []
    for i in range(n_agents):
        #Create an agent
        agents.append(af.Agent(agents, i, environment, n_rows, n_cols))
        print(agents[i])
    #print(agents)

    #%% MOVE AGENTS
    # Model loop
    #Create directory to write images to
    try:
        os.makedirs('../../data/output/images/')
    except FileExistsError:
        print("path exists")

    # For storing images
    global ite                    
    ite = 0
    images = []
    for ite in range(n_iterations):
        print("Iteration", ite)
        # Move agents
        print("Move")
        for i in range(n_agents):
            agents[i].move(x_min, y_min, x_max, y_max)
            agents[i].eat()
            #print(agents[i])
        # Share store
        # Distribute shares
        for i in range(n_agents):
            agents[i].share(neighbourhood)
        # Add store_shares to store and set store_shares back to zero
        for i in range(n_agents):
            #print(agents[i])
            agents[i].store = agents[i].store_shares
            agents[i].store_shares = 0
        print(agents)
        # Print the maximum distance between all the agents
        print("Maximum distance between all the agents", get_max_distance(agents))
        # Print the total amount of resource
        sum_as = addup_store(agents)
        print("sum_agent_stores", sum_as)
        sum_e = addup_environment(environment)
        print("sum_environment", sum_e)
        print("total resource", (sum_as + sum_e))
        
        #%%DRAW PLOTS
        # Plot

        #background
        plt.imshow(environment)

        # points
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

        #flip y-axis back
        plt.ylim(y_max/3, y_max*2/3)
        plt.xlim(x_max/3, y_max*2/3)
        
        #Save the image to png format files
        filename = '../../data/output/images/image' + str(ite) + '.png'
        #filename = '../../data/output/images/image' + str(ite) + '.gif'
        plt.savefig(filename)
        plt.show()
        plt.close()
        images.append(imageio.imread(filename))
        
    imageio.mimsave('../../data/output/out.gif', images, fps=3)

    #%% CALCULATIONS
    # Calculate the environment and store
    # sum_store = addup_store(agents)
    # sum_env = addup_environment(environment)

    # print(sum_store, sum_env, sum_store+sum_env)

    #record the start time 
    # start = time.perf_counter()

    # #Start to get distance and the max distance
    # get_max_distance(agents)

    # #reord the end time
    # end = time.perf_counter()
    # #print("Time taken to calculate maximum distance", end - start, "seconds")
    # #%%OUTPUT
    # write_in(environment)


