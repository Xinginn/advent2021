#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 10:59:23 2021

@author: felix
"""

fishes = open("./input.txt").readline().replace('\n', '').split(',')
timers = [0] * 9

for fish in (fishes):
  timers[int(fish)] += 1
  

for i in range(256):
  new_timers = [0] * 9
  for i in range(8, 0, -1):
    if i == 1:
      new_timers[8] += timers[0]
      new_timers[6] += timers[0]
    new_timers[i-1] = timers[i]
  timers = new_timers
  
print(sum(timers))
  
