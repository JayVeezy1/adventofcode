# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:34:37 2020

@author: Jakob
"""
import re

liste = []
    
with open(r'C:\Users\vanek\Desktop\AdventOfCode\data\data_2.csv') as file:
    for row in file:
        liste.append(row)
    for row in range(0, len(liste)):
        liste[row] = re.split('[- : \s]', liste[row])
        for i in range(0, len(liste[row])-1):
            if (liste[row][i] == ''):    
                del liste[row][i]

correct = 0
for row in range(0, len(liste)):
    pos1 = int(liste[row][0])
    pos2 = int(liste[row][1])
    print("pw:", liste[row][3])
    print("gesucht: ", liste[row][2])
    print(int(liste[row][0]), "-", int(liste[row][1]))
    # wichtig: auf index achten!
    if(liste[row][3][pos1 - 1] == liste[row][2]):
        if(liste[row][3][pos2 - 1] == liste[row][2]):
            print("matches both - wrong")
        else:
            print("only machtes pos1")
            correct += 1
    elif(liste[row][3][pos2 - 1] == liste[row][2]):
        print("only matches pos2")
        correct += 1
    else:
        print("matches none")
            
print("Korrekte PW:", correct)  