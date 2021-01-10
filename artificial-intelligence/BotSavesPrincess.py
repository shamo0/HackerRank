#!/usr/bin/python

'''
Author: shamo0

Princess Peach is trapped in one of the four corners of a square grid.
You are in the center of the grid and can move one step at a time in 
any of the four directions. Can you rescue the princess?

Input format
The first line contains an odd integer N (3 <= N < 100) denoting the 
size of the grid. This is followed by an NxN grid. Each cell is denoted
by '-' (ascii value: 45). The bot position is denoted by 'm' and the
princess position is denoted by 'p'.

Grid is indexed using Matrix Convention

Output format
Print out the moves you will take to rescue the princess in one go.
The moves must be separated by '\n', a newline. The valid moves are
LEFT or RIGHT or UP or DOWN.
'''
def displayPathtoPrincess(n,grid):
    n = n-1
    
# #print all the moves here
    current_x = n//2
    current_y = n//2
   
    
    if grid[0][0] =='p':
        while grid[current_y][current_x] != 'p':
            print('LEFT')
            print('UP')
            current_x-=1
            current_y-=1
            if grid[current_y][current_x] =='p':
                break
    elif grid[0][n] =='p':
        while grid[current_y][current_x] != 'p':
            print('RIGHT')
            print('UP')
            current_x+=1
            current_y-=1
            if grid[current_y][current_x] =='p':
                break
    elif grid[n][0] == 'p':
        while grid[current_y][current_x] != 'p':
            print('LEFT')
            print('DOWN')
            current_x-=1
            current_y+=1
            if grid[current_y][current_x] =='p':
                break
    elif grid[n][n] == 'p':
        while grid[current_y][current_x] != 'p':
            print('RIGHT')
            print('DOWN')
            current_x+=1
            current_y+=1
            if grid[current_y][current_x] =='p':
                break
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
