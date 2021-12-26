#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 11:22:06 2021

@author: felix
"""

max_value = 0

crabs = open("./input.txt").readline().replace('\n', '').split(',')
for i in range(len(crabs)):
  value = int(crabs[i])
  crabs[i] = value
  if value > max_value:
    max_value = value

lowest_fuel_need = 9999999
cheapest_position = 0

for i in range(max_value):
  fuel = 0
  for crab in crabs:
    fuel += abs(crab - i)
  if fuel < lowest_fuel_need:
    lowest_fuel_need = fuel
    cheapest_position = i

print(cheapest_position)
print(lowest_fuel_need)
    