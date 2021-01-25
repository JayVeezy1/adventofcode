# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:49:44 2020

@author: Jakob
"""

with open (r'C:\Users\vanek\Desktop\AdventOfCode\data\data_10.txt') as file:
    data = file.read().splitlines()
    data = [0] + sorted(int(i) for i in data)
    data.append(max(data) + 3)
    
diffs = [b-a for a, b in zip(data, data[1:])]           # was ist dieses zip eigentlich?
print(diffs.count(1) * diffs.count(3))
