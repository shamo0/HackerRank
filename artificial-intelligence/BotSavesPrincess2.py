'''
***Task***

Complete the function nextMove which takes in 4 parameters - an integer N, 
integers r and c indicating the row & column position of the bot and the 
character array grid - and outputs the next move the bot makes to rescue the princess.

***Input Format***

The first line of the input is N (<100), the size of the board (NxN). The second
line of the input contains two space separated integers, which is the position of the bot.

Grid is indexed using Matrix Convention

The position of the princess is indicated by the character 'p' and the position 
of the bot is indicated by the character 'm' and each cell is denoted by '-' (ascii value: 45).

***Output Format***

Output only the next move you take to rescue the princess. Valid moves are LEFT, RIGHT, UP or DOWN

Author: shamo0
'''
def nextMove(n,r,c,grid):
    location_row = 0
    location_col = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'p':
                location_row = i
                location_col = j
                
    if location_col > c:
        return("RIGHT")
    elif location_col < c:
        return("LEFT")
    elif location_row < r:
        return("UP")
    elif location_row > r:
        return("DOWN")
    
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
