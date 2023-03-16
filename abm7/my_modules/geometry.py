# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:06:11 2023

@author: ASUS
"""
import math

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