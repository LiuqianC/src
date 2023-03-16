# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:24:44 2023

@author: ASUS
"""
import csv

def read_data(filename):
    '''
    

    Parameters
    ----------
    filename : string
        The path of the csv input file.

    Returns
    -------
    n_rows : int
        To indentify how many rows are there.
    n_cols : int
        To indentify how many colums are there.
    data : list
        The csv input file will store in the list 'data'.

    '''
    # Read input data
    f = open(filename, newline='')
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

def write_data(filename,data):
    '''
    

    Parameters
    ----------
    filename : string
        The path of the csv output file.
    data : list
        The output csv file

    Returns
    -------
    None.

    '''
    
    f = open(filename,'w', newline='')
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row) #list of values
    f.close()
