#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:13:00 2021

@author: felix
"""

total_upward = 0;
previous = None

for current in open("./input.txt").readlines():
  current = int(current)

  if previous:
    total_upward += 1 if previous < current else 0
    
  previous = current

print(total_upward)
