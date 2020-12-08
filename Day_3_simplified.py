# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:28:53 2020

@author: Jakob
"""
# 1) Erstelle einen String mit komplettem Input
liste = []  
with open(r'C:\Users\vanek\Desktop\AdventOfCode\data\data_3.txt') as file:
    liste = file.read().splitlines()
text = ""
for cell in range(0, len(liste)): 
    text = text + liste[cell] 

# 2) Benoetigte Variabeln
# 3 = 3 nach rechts
# 31 = 1 nach unten
trees = 0 
pos = 0
right = 3
down = 31
  
# 3) Iteriere bis Ende vom String
#   wenn "#" dann zaehle trees
#   ansonsten gehe 3 und dann 31 Schritte weiter
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
    
print(trees)
# mein Ergebnis = 137 die Lösung war aber glaube ich 259? 
# Ich erinner mich nicht mehr dran