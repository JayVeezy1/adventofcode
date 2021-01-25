# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 12:42:20 2020

@author: Jakob
 """
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

values= ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",]  
# cid is optional!

# import data
with open(r'C:\Users\vanek\Desktop\AdventOfCode\data\data_4.txt') as file:
    raw_data = file.read().split('\n\n')

# format data into clean list
temp = []
for person in raw_data:
    temp.append(person.replace('\n', ' ').split(' '))   
# print(temp)

# transfer list into temp dict - directly check required fields
counter = 0
for p in temp:
    d = dict(i.split(':') for i in p)
    if(all(v in d for v in values)):
            counter += 1

print(counter)

