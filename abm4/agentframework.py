# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:41:15 2023

@author: ASUS
"""
import random

class Agent():
    
    def __init__(self,i):
        '''
        The constructor method.
        
        Parameters
        -------
        i : Integet
            To be unique to each instance.

        Returns
        -------
        None.

        '''
        self.i = i
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
    
    def __str__(self):
        return str(self.i)
        #return self.__class__.__name__ + "(x=" + str(self.x)\
        #    + ", y=" + str(self.y) + ")"
            
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
        if self.x < x_min:
            self.x = x_min
        if self.y < y_min:
            self.y = y_min
        if self.x > x_max:
            self.x = x_max
        if self.y > y_max:
            self.y = y_max