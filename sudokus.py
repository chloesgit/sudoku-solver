import numpy as np

# Sudokus to solve. The Program solves S by default

# Template
S0 = np.array(  [[0,0,0,  0,0,0,  0,0,0],
                [0,0,0,  0,0,0,  0,0,0],
                [0,0,0,  0,0,0,  0,0,0],
                
                [0,0,0,  0,0,0,  0,0,0],
                [0,0,0,  0,0,0,  0,0,0],
                [0,0,0,  0,0,0,  0,0,0],
                
                [0,0,0,  0,0,0,  0,0,0],
                [0,0,0,  0,0,0,  0,0,0],
                [0,0,0,  0,0,0,  0,0,0]])
     
# Default sudoku solved
S = np.array(   [[0,0,3, 0,0,0, 5,0,7],
                 [8,4,5, 0,0,0, 2,0,0],
                 [0,0,0, 0,1,9, 0,0,0],
                 
                 [3,2,1, 0,7,0, 0,0,0],
                 [4,0,0, 0,0,0, 0,5,3],
                 [0,0,0, 0,4,1, 0,0,0],
                 
                 [0,5,0, 0,0,0, 8,4,0],
                 [2,9,0, 0,0,6, 0,0,0],
                 [1,0,0, 2,5,4, 0,0,0]])

# Stock here sudokus :)
T = np.array(   [[1,0,0,  0,0,7,  0,9,0],
                 [0,3,0,  0,2,0,  0,0,8],
                 [0,0,9,  6,0,0,  5,0,0],
                 
                 [0,0,5,  3,0,0,  9,0,0],
                 [0,1,0,  0,8,0,  0,0,2],
                 [6,0,0,  0,0,4,  0,0,0], # Hardest sudoku in the world
                 
                 [3,0,0,  0,0,0,  0,1,0],
                 [0,4,1,  0,0,0,  0,0,7],
                 [0,0,7,  0,0,0,  3,0,0]])

R = np.array(   [[0,1,0,  0,0,0,   0,0,8],
                 [0,0,6,  0,0,5,  9,0,7],
                 [0,0,2,  3,8,0,  6,0,1],
                 
                 [0,0,0,  9,0,0,  0,0,0],
                 [0,0,0,  8,0,0,  5,0,0],
                 [9,8,0,  5,6,7,  1,0,0],
                 
                 [0,0,0,  7,0,0,  0,0,0],
                 [0,0,9,  0,0,0,  0,0,0],
                 [0,0,8,  1,9,0,  2,0,6]])


U = np.array(   [[0,7,5,  0,9,0,  0,0,6],
                 [0,2,3,  0,8,0,  0,4,0],
                 [8,0,0,  0,0,3,  0,0,1],
                 
                 [5,0,0,  7,0,2,  0,0,0],
                 [0,4,0,  8,0,6,  0,2,0],
                 [0,0,0,  9,0,1,  0,0,3],
                 
                 [9,3,0,  4,0,0,  0,0,7],
                 [0,6,0,  0,7,0,  5,8,0],
                 [7,0,0,  0,1,0,  3,9,0]])

V = np.array(   [[8,3,0,  9,0,5,  0,1,7],
                 [0,0,0,  0,0,0,  0,8,3],
                 [7,0,1,  8,4,0,  6,0,0],
                 
                 [4,0,0,  1,0,6,  0,0,0],
                 [1,0,0,  0,0,0,  9,0,0],
                 [0,0,6,  0,0,0,  8,7,0],
                 
                 [0,9,7,  0,0,0,  0,2,0],
                 [6,4,0,  0,0,7,  0,5,0],
                 [0,0,0,  0,0,9,  0,4,8]])