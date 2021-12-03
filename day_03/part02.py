#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 22:30:47 2021

@author: felix
"""
oxygen = []
carbon = []

lines = open("./input.txt").readlines()

def filter_oxygen(source_ox, position):
  ones = []
  zeroes = []
  for line in source_ox:
    if line[position] == "1":
      ones.append(line)
    else:
      zeroes.append(line)
  return ones if len(ones) >= len(zeroes) else zeroes

def filter_carbon (source_car, position):
  ones = []
  zeroes = []
  for line in source_car:
    if line[position] == "1":
      ones.append(line)
    else:
      zeroes.append(line)
  return ones if len(ones) < len(zeroes) else zeroes
  
oxygen = filter_oxygen(lines, 0)
carbon = filter_carbon(lines, 0)

pos = 1
while(len(oxygen) != 1):
  oxygen = filter_oxygen(oxygen, pos)
  pos += 1
  
pos = 1
while(len(carbon) != 1):
  carbon = filter_carbon(carbon, pos)
  pos += 1

print(int(oxygen.pop(-1),2) * int(carbon.pop(-1),2))