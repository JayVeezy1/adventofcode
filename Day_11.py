# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 20:09:39 2020

@author: Jakob
"""
import itertools

def count_seated(seats):
    return list(itertools.chain(*seats)).count('#')

def count_adjacent_seats(row_id, col_id, seats):
    counter = 0
    adjacent = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    # adjacent = [(i, j) for i, j in itertools.product(range(-1, 2, 1), repeat = 2) if i != 0 or j != 0]
    for off_i, off_j in adjacent:
        if 0 <= row_id + off_i < len(seats) and 0 <= col_id + off_j < len(seats[row_id + off_i]) and seats[row_id + off_i][col_id + off_j] == "#":
            counter += 1
    return counter


def simulate(seats):
    previous = []
    
    while previous != seats:
        previous = seats[:]
        seats = []
        for row_id, row in enumerate(previous):
            new_row = ""
            for col_id, col in enumerate(row):
                if col == ".":
                    new_row += col
                elif col == "L":
                    if count_adjacent_seats(row_id, col_id, previous) == 0:
                        new_row += "#"
                    else:
                        new_row += "L"
                elif col == "#":
                    if count_adjacent_seats(row_id, col_id, previous) >= 4:
                        new_row += "L"
                    else:
                        new_row += "#"
                else:
                    new_row += col
            seats.append(new_row)
        assert len(previous) == len(seats)
        assert len(previous[0]) == len(seats[0])
    return previous

with open(r'C:\Users\vanek\Desktop\AdventOfCode\data\data_11.txt') as file:
    seats = file.read().splitlines()
waiting_room = simulate(seats)
print(count_seated(waiting_room))



