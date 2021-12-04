#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 17:52:15 2021

@author: felix
"""
class Cell:
  def __init__(self, value):
    self.value = int(value)
    self.marked = False

class Board:
  def __init__(self, rows):
    self.rows = []
    self.unmarked_sum = 0
    for row in rows:
      new_row = []
      for i in range(5):
        value = int(row[i])
        new_row.append(Cell(value))
        self.unmarked_sum += value
      self.rows.append(new_row)
        
  def mark_and_check_winner(self, number):
    for row in self.rows:
      for cell in row:
        if cell.value == number:
          cell.marked = True
          self.unmarked_sum -= number
          if self.is_winner():
            return(number)
    return(-1)
  
  def is_winner(self):
    for row in self.rows:
      marked_number = 0
      for cell in row:
        marked_number += int(cell.marked)
      if marked_number == 5:
        return(True)
    
    for col_number in range(5):
      marked_number = 0
      for row in self.rows:
        marked_number += int(row[col_number].marked)
      if marked_number == 5:
        return(True)


lines = open("./input.txt").readlines()

boards = []
numbers = lines.pop(0).replace('\n', '').split(',')

while len(lines) > 5:
  lines.pop(0)
  rows = []
  for i in range(5):
    rows.append(' '.join(lines.pop(0).split()).split(' '))
    
  boards.append(Board(rows))

def roll():
  for num in numbers:
    num = int(num)
    for board in boards:
      if board.mark_and_check_winner(num) > -1:
        return(board.unmarked_sum * num)

  
print(roll())  
  
