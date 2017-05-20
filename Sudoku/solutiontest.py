# -*- coding: utf-8 -*-
"""
Created on Sat May 20 09:56:12 2017

@author: Petruska
"""

from utils import *
from solution import *

grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
values = grid_values(grid)
values = grid_values(grid2)


values = reduce_puzzle(values)
display(values)
solved_values = [box for box in values.keys() if len(values[box]) == 1]
unsolved_values = [box for box in values.keys() if len(values[box]) >1 ]
print (len(values))
print (solved_values)
print (len(solved_values))
print (unsolved_values)
print (len(unsolved_values))
ll = dict(zip(unsolved_values, [len(values[box]) for box in unsolved_values]))
m = min(ll, key = ll.get)
print ('M',  m)
print (values[m])

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    values = reduce_puzzle(values)
    if (values == False):
#        print ('returning false')
        return values
#    print('=================================================================================================')
#    display(values)
    # Choose one of the unfilled squares with the fewest possibilities
    unsolved_values = [box for box in values.keys() if len(values[box]) >1 ]
    if (len(unsolved_values) == 0 ):
        return values
    lenUnsolved = dict(zip(unsolved_values, [len(values[box]) for box in unsolved_values]))
#    minBoxes = sorted(lenUnsolved, key = lenUnsolved.get)
    minBox = min(lenUnsolved, key = lenUnsolved.get)
#    print ('minBox list' , minBoxes)
    
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
#    for minBox in minBoxes:
    for v in values[minBox]:
        new_sudoku = values.copy()
#        print ('minBox ', minBox, 'value ', v)
        new_sudoku[minBox] = v
        res = search(new_sudoku)
        if res:
            return res
    return False
    # If you're stuck, see the solution.py tab!



resValues = search(values)
display(resValues)