# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:41:15 2023

@author: ASUS
"""
import random

class Agent():
    
    def __init__(self, i, environment, n_rows, n_cols):
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
        self.i = i
        self.environment = environment
        self.x = random.randint(n_cols/3 - 1, 2 * n_cols / 3)
        self.y = random.randint(n_rows/3 - 1, 2 * n_rows / 3)
        self.store = 0
    
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