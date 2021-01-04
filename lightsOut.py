'''
Lights Out is a game of cellular automaton where a cell and all its 
defined neighbors changes states on firing it.
In this version of Lights Out, 2 players compete against each other 
by firing the cells on an 8x8 grid. Each cell has 2 states.

ON indicated by the number 1
OFF indicated by the number 0
A cell at (r,c) on firing changes its state and 2 of its neighbors, 
the one towards its right (r,c+1) and the one below (r+1,c).

You are allowed only to fire at cells that are ON.

Input Format

Top left cell of the grid is indexed as (0,0) and the bottom right 
of the grid is indexed at (7,7). The 1st player is represented by 
the number 1 and the 2nd player is represented by the number 2.

The first line of input contains the number of the current player.
8 lines follow, each line containing 8 integers without any space 
between them. Each integer can be either 0 or 1 representing the 2
states of the cell.

Output Format

You are required to output two single spaced integers that is the 
position of the cell you wish to fire.
'''

def nextmove(player,grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                print(i,j)
                return

n = int(input())
grid = []
for i in range(0, 8):
    grid.append(input())
    
nextmove(n,grid)
