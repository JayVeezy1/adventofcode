# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:08:13 2020

@author: Jakob
"""
# Day 2:
x1 = 0
x2 = 0
x3 = 0
    
text_file = open(r'C:\Users\vanek\Desktop\AdventOfCode\data\data_1.txt')
liste = text_file.readlines()
# print(liste) 

for i in liste:
    for j in liste:
        for k in liste:
            if (int(i)  + int(j) + int(k)== 2020):
                x1 = int(i)
                x2 = int(j)
                x3 = int(k)
                break
solution = x1 * x2 * x3

print("Werte: ",x1, x2, x3, "Ergebnis: ", solution)