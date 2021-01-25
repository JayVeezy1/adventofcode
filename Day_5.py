# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:12:26 2020

@author: Jakob
"""
# part 1 - find highest seat ID:

with open(r'C:\Users\vanek\Desktop\AdventOfCode\data\data_5.txt') as file:
    seats_original = file.read().splitlines()
    # print(seats)

seats = []

# super gute Lsg! Nicht in den Reihen rumrechnen und Schrittweise aufteilen
# Sondern 'Binaere-Suche' nutzen. Bedeutet 'richtungsanweisung' in binaer umwandeln
# und das einfach als decimal-zahl = Reihe
for i in seats_original:
    row = int(i[:7].replace('F', '0').replace('B', '1'), 2)
    column = int(i[-3:].replace('L', '0').replace('R', '1'), 2)
    seat_id = row * 8 + column
    # print("row=", row)
    # print("columns", column)
    # print(seat_id)
    seats.append(seat_id)
    
print(max(seats)) 
# 959

# part 2:
liste = []
for i in range(0, 127):
    for x in range(1, 8):
        potential = i * 8 + x
        liste.append(potential)
    
for i in liste:
    if not i in seats:
        x1 = i + 1
        x2 = i - 1
        if x1 in seats:
            if x2 in seats:
                print("possibly: ", i)       
# 527
            