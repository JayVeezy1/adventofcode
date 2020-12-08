# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:20:03 2020

@author: Jakob
"""
import math

liste = []  
with open(r'C:\Users\vanek\Desktop\AdventOfCode\data\data_3.txt') as file:
    liste = file.read().splitlines()
  
trees = 0 
text = ""
pos = 0
slopes = [1, 3, 5, 7, 1]
steep = [1, 1, 1, 1, 2]
hits = [0, 0, 0, 0, 0]

for cell in range(0, len(liste)): 
    text = text + liste[cell]   

for s in range(0, 5):
    pos = 0
    trees = 0
    right = int(slopes[s])
    down = int(steep[s]) * 31
    #print(right, down)
    #print(math.floor(len(text) / (right + down)))

    while (pos + right <= len(text) - 1):
        if (pos + right + down <= len(text) - 1):
            if (text[pos] == '#'):
                trees += 1
            pos += right
            if (text[pos] == '#'):
                trees += 1
            pos += down
        else:
            if (text[pos] == '#'):
                trees += 1
            pos += right
            if (text[pos] == '#'):
                trees += 1
            continue
    hits[s] = trees    
    print(hits[s])
        
result = math.prod(hits)
print("hits: ", result)

print(result/2224913600)
# 15.173.982.450 is too high! Solution: 2.224.913.600