#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:13:00 2021

@author: felix
"""

total_upward = 0;
previous = None

for current in open("./01_input.txt").readlines():
  current = int(current)
  
  if previous:
    total_upward += 1 if previous < current else 0
    
  previous = current
  

print(total_upward) # pourquoi suis-off de 1?



"""
total_upward = 0;

previous = -1
ante_previous = -1
current_sum = -1
previous_sum = -1

for current in open("./01_input.txt").readlines():
  current = int(current)
  if previous > 0 and ante_previous > 0:
    current_sum = previous + ante_previous + current
  
  if previous_sum > 0:
    total_upward += 1 if previous_sum < current_sum else 0
    
  previous_sum = current_sum
  
  ante_previous = previous
  previous = current
  

print(total_upward) # pourquoi suis-off de 1?

"""