#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 23:25:53 2021

@author: felix
"""

fishes = open("./input.txt").readline().replace('\n', '').split(',')
days = [0] * 9

for fish in (fishes):
  days[int(fish)] += 1
  
print(days)

for i in range(60):
  new_days = [0] * 9
  for i in range(8, 0, -1):
    if i == 1:
      new_days[8] += days[0]
      new_days[6] += days[0]
    new_days[i-1] = days[i]
  days = new_days
  
print(sum(days))