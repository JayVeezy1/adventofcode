# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:21:36 2020

@author: Jakob
"""
import re

with open(r'C:\Users\vanek\Desktop\AdventOfCode\data\data_7.txt') as file:
    lines = file.read().splitlines()
# print(lines)

# man sollte einen Graph/Baum nutzen, nicht mit Listen rumversuchen
# graph wird indirekt aus dictionary erstellt
graph = {}

for i in lines:
    regexy = re.match('(.+?) bags', i)
    color_primary = regexy.group(1)
    color_inside = re.findall('(\d+) (.+?) bag', i)
    if len(color_inside) > 0:                                   # wenn 'no other' dann color_inside = [] dann keine ausgehenden kanten - einfach weglassen
        color_inside = list(list(zip(*color_inside))[1])        # starker trick mit dem * !!!
        graph[color_primary] = color_inside
    else:
        graph[color_primary] = []
    print("primary: ", color_primary)
    print(color_inside)

# erste Idee war for i in graph: aber komplett jeden Knoten durchsuchen ist sehr ineffizient!
# Deshalb rekursiv loesen - genial!
def shiny_gold(color):
    if color == "shiny gold":
        return True
    else:
        return any(shiny_gold(child) for child in graph[color])

print("part1: ", sum(shiny_gold(color) for color in graph.keys()) - 1)
# print(graph)

# part 2 - skipped.