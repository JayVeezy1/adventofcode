# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:16:50 2020

@author: Jakob
"""
END = 0
def check_match(pos, start, lines):
    previous = lines[start:pos]             ## ahhh das ist ohne obere kante also end index - 1
    previous = list(map(int, previous))
    # print('\n check for: ', lines[pos], 'in prev: ', previous)
    for i in range(0, 24):
        difference = abs(int(lines[pos]) - int(lines[start + i]))
        if difference in previous:
            if difference != int(lines[pos]) / 2:
                return True
    return False


# alternative: raw_data = file.read().split('\n\n')
with open(r'C:\Users\vanek\Desktop\AdventOfCode\data\data_9.txt') as file:
    lines = file.read().splitlines()
    
pos = 25
for i in range(len(lines)):
    start = pos - 25
    if (check_match(pos, start, lines)):
        pos += 1
        i += 1
    else:
        print("no matches found for:", lines[pos])
        break

# part 1 Lsg: 393911906

# part 2
def check_adding(i, lines):
    global END
    rest = lines[i:]
    rest = list(map(int, rest))
    for j in range(1, len(rest)):
        if sum(rest[:j]) == 393911906:
            END = j + i
            return True
        
    return False
            

x = 393911906
for i in range(len(lines)):
    if (check_adding(i, lines)):
        solution = min(list(map(int, lines[i:END]))) + max(list(map(int, lines[i:END])))
        print('set found! starting at idx: ', i, 'to end-idx: ', END, 'with lowest-value: ', min(lines[i:END]), 'and highest-value ', max(lines[i:END]))
        print('solution is: ', solution)
        break
     # else:
        # print('no add up for: ', i)
    
