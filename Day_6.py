# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:44:41 2020

@author: Jakob
"""
import string

with open(r'C:\Users\vanek\Desktop\AdventOfCode\data\data_6.txt') as file:
    raw_data = file.read().split('\n\n')
    
clean_data = []
for field in range(0, len(raw_data)):
    raw_data[field] = list(raw_data[field].split('\n'))
# print(raw_data)

clean_data = raw_data
# gruppe = clean_data
# count = []
# for gr in range(0, len(raw_data)):
#     temp = []
#     for person in range(0, len(raw_data[gr])):
#         temp = str(temp) + raw_data[gr][person]
#     temp = temp.strip('[]')
#     gruppe[gr] = temp
#     count.append(len(set(gruppe[gr])))
    
# print(sum(count))
# Lsg: 6565


# part two everyone answers 'yes' - eher schlecht designed! aber lsg stimmt.
print(clean_data)
bool_counter = []
counter = 0
for letter in string.ascii_lowercase[:26]:
    for pos in range(0, len(clean_data)):
        if all(letter in s for s in clean_data[pos]):
            counter += 1
            print("for group: ", clean_data[pos], "\n answer", letter, "is True")
print(counter)     
# Lsg: 3137        