#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:36:39 2021

@author: felix
"""

total_upward = 0;

previous = None
ante_previous = None
current_sum = None
previous_sum = None

for current in open("./input.txt").readlines():
  current = int(current)
  if previous and ante_previous:
    current_sum = previous + ante_previous + current
  
  if previous_sum:
    total_upward += 1 if previous_sum < current_sum else 0
    
  previous_sum = current_sum
  
  ante_previous = previous
  previous = current
  

print(total_upward)