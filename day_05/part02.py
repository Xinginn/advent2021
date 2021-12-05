#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:47:55 2021

@author: felix
"""
area = [ [0] * 999 for i in range(999)]

total = 0

for line in open("./input.txt").readlines():
  
  coords = line.replace('\n', '').replace(' -> ', ',').split(',')
  for i in range(4):
    coords[i] = int(coords[i])
  
  if coords[0] == coords[2]: # X1 == X2 donc horizontal
    x = coords[0]
    step = -1 if coords[3] < coords[1] else 1
    for y in range(coords[1], coords[3] + step, step):
      area[x][y] += 1
      total += 1 if area[x][y] == 2 else 0

  elif coords[1] == coords[3]: # vertical
    y = coords[1]
    step = -1 if coords[2] < coords[0] else 1
    for x in range(coords[0], coords[2] + step, step):
      area[x][y] += 1
      total += 1 if area[x][y] == 2 else 0
      
  else: # diagonal  
    x_step = 1 if coords[2] > coords[0] else -1
    y_step = 1 if coords[3] > coords[1] else -1
    delta = abs(coords[0]-coords[2])
    for i in range(delta + 1):
      x = coords[0] + i * x_step
      y = coords[1] + i * y_step
      area[x][y] += 1
      total += 1 if area[x][y] == 2 else 0

print(total)