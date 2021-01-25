# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 21:30:14 2020

@author: Jakob
"""
DIRECTION = "E"
X = 0
Y = 0

def move_forward(line):
    global DIRECTION
    global X
    global Y
    print("doing move_forward")
    if DIRECTION == "N":
        Y += int(line[1:])
    elif DIRECTION == "S":
        Y -= int(line[1:])
    elif DIRECTION == "E":
        X += int(line[1:])
    elif DIRECTION == "W":
        X -= int(line[1:])
    else:
        pass
    
def turn_right():
    print("doing turn_right")
    global DIRECTION
    if DIRECTION == "N":
        DIRECTION = "E"
    elif DIRECTION == "S":
        DIRECTION = "W"
    elif DIRECTION == "E":
        DIRECTION = "S"
    elif DIRECTION == "W":
        DIRECTION = "N"
    else:
        pass
    
def turn_left():
    print("doing turn_left")
    global DIRECTION
    if DIRECTION == "N":
        DIRECTION = "W"
    elif DIRECTION == "S":
        DIRECTION = "E"
    elif DIRECTION == "E":
        DIRECTION = "N"
    elif DIRECTION == "W":
        DIRECTION = "S"
    else:
        pass
    
def turn_around():
    print("doing turn_around")
    global DIRECTION
    if DIRECTION == "N":
        DIRECTION = "S"
    elif DIRECTION == "S":
        DIRECTION = "N"
    elif DIRECTION == "E":
        DIRECTION = "W"
    elif DIRECTION == "W":
        DIRECTION = "E"
    else:
        pass

with open (r'C:\Users\vanek\Desktop\AdventOfCode\data\data_12.txt') as file:
    data = file.read().splitlines()

counter = 0
for line in data:
    counter += 1
    print(line)
    if line[:1] == "N":
        print(line[1:])
        Y += int(line[1:])
    elif line[:1] == "S":
        Y -= int(line[1:])
    elif line[:1] == "E":
        X += int(line[1:])
    elif line[:1] == "W":
        X -= int(line[1:])
    elif line[:1] == "F":
        move_forward(line)
    elif line[:1] == "R":
        if line[1:] == "180":
            turn_around()
        elif line[1:] == "270":
            turn_left()
        else:
            turn_right()
    elif line[:1] == "L":
        if line[1:] == "180":
            turn_around()
        elif line[1:] == "270":
            turn_right()
        else:
            turn_left()
    else:
        print("problem")
        break
    print(X, Y, DIRECTION, "\n")
    
print("inputs: ", len(data), "counter: ", counter)
    
manhattan_distance = abs(X) + abs(Y)
print("Manhattan Distance:", manhattan_distance)
