# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:24:44 2023

@author: ASUS
"""

def read_data():
    
    import csv

    # Read input data
    f = open('../../data/input/in.txt', newline='')
    data = []
    n_rows = 0
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        n_rows += 1
        n_cols = 0
        for value in line:
            row.append(value)
            n_cols += 1
            #print(value)
        data.append(row)
    f.close()
    #print(data)
    return n_rows, n_cols, data
