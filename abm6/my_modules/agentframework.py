# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:41:15 2023

@author: ASUS
"""
import random
import my_modules.geometry as gm

class Agent():
    
    def __init__(self, agents, i, environment, n_rows, n_cols):
        '''
        The constructor method.
        
        Parameters
        -------
        i : Integer
            To be unique to each instance.
        n_rows : Integer
            The number of rows in environment
        n_cols : Integer
            The number of columns in environment

        Returns
        -------
        None.

        '''
        self.agents = agents
        self.i = i
        self.environment = environment
        tnc = int(n_cols / 3)
        self.x = random.randint(tnc - 1, (2 * tnc) - 1)
        tnr = int(n_rows / 3)
        self.y = random.randint(tnr - 1, (2 * tnr) - 1)
        self.store = 0
        self.store_shares = 0
    
    def __str__(self):
        #return str(self)
        return self.__class__.__name__ +"NO." + str(self.i) + "(x=" + str(self.x)\
            + ", y=" + str(self.y) + ")"
            
    def __repr__(self):
        return str(self)
    
    def move(self, x_min, y_min, x_max, y_max):
        # Move agents
        # Change agents[i] coordinates randomly
        #x-coordinate
        rn = random.random()
        if rn <0.5:
            self.x += 1
        else:
            self.x -= 1
        #y-coordinate
        rn = random.random()
        if rn<0.5:
            self.y += 1
        else:
            self.y -= 1
        # Movement constraits
        if self.x < x_min:
            self.x = x_min
        if self.y < y_min:
            self.y = y_min
        if self.x > x_max:
            self.x = x_max
        if self.y > y_max:
            self.y = y_max
        return self.x, self.y
    
    def eat(self):
        '''
        
        Returns
        -------
        None.

        '''
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x]=0
            
    def share(self, neighbourhood):
        # Create a list of agents in neighbourhood
        neighbours = []
        #print(self.agents[self.i])
        for a in self.agents:
            distance = gm.get_distance(a.x, a.y, self.x, self.y)
            if distance < neighbourhood:
                neighbours.append(a.i)#neibhbours stores agents' index
        # Calculate amount to share
        n_neighbours = len(neighbours)
        #print("n_neighbours", n_neighbours)
        shares = self.store / n_neighbours
        #print("shares", shares)
        # Add shares to store_shares
        for i in neighbours:
            self.agents[i].store_shares += shares