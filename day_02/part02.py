#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 08:02:39 2021

@author: felix
"""
aim = 0
depth = 0
x = 0

for line in open("./input.txt").readlines():
  delta = int(line[-2])  # -2 puisque -1 est \n
  if line[0] == 'f':
    x += delta
    depth += aim * delta
  else:
    aim += delta if line[0] == 'd' else delta * -1
  

print(depth, x)
print(depth * x)