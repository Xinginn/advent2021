#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:20:13 2021

@author: felix
"""

gamma = ""
epsilon = ""

columns = [0 for i in range(12)]

for line in open("./input.txt").readlines():
  for i in range(12):
    columns[i] += int(line[i])
  
for col in columns:
  gamma += str(int(col > 500))
  epsilon += str(int(col < 500))
  
  
print(int(gamma,2) * int(epsilon,2))