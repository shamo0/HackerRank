'''
Author: shamo0

Tron is a two player game based on the popular movie Tron. The objective 
of the game is to cut off players movement through each others motorbikes 
that leave a wall behind them as they move.

Input Format
This version of Tron takes place on a 15x15 grid. Top left of the grid is 
(0,0) and the bottom right of the grid is indexed as (14,14).
The 1st player is represented by r (ascii value 114) and is positioned with
his bike at (7,1) and the 2nd player is represented by g (ascii value 103) 
and is positioned with his bike at the opposite end of the grid at (7,13).

The first line contains a character representing the current player.
The second line consists of four single spaced integers representing the 
current position of the 1st and 2nd players' motorbike.
15 lines follow which represents the grid map.
Boundary is represented by # (ascii value 35), an empty grid is represented by 
- (ascii value 45). Wall left behind by the player are represented by their 
respective characters.

Output Format
Player's are allowed to output any one of the following moves as the movement of their motorbikes.

LEFT
RIGHT
UP
DOWN
'''

def nextmove(grid, player1_pos, player2_pos):
    y = int(player1_pos[1])
    x = int(player2_pos[0])
    # if (grid[x][y+1] == '-') and (grid[x][y+1] != '#') and (grid[x][y+1] != 'r') and (grid[x][y+1] != 'g'):
    #     print('DOWN')
    # elif (grid[x+1][y] == '-') and (grid[x+1][y] != '#') and (grid[x+1][y] != 'r')  and (grid[x+1][y] != 'g'):
    #     print('RIGHT')
    # elif (grid[x][y-1] == '-') and (grid[x][y-1] != '#') and (grid[x][y-1] != 'r') and (grid[x][y-1] != 'g'):
    #     print('UP')
    # elif (grid[x-1][y] == '-') and (grid[x-1][y] != '#') and (grid[x-1][y] != 'r') and (grid[x-1][y] != 'g'):
    #     print('LEFT')
    # print(grid[x+1][y])
    if grid[x+1][y] == '-':
        print('DOWN')
    elif grid[x+1][y] == 'g' or grid[x+1][y] == 'r' or grid[x+1][y] == '#':
        if (grid[x][y+1] == '-'):
            print('RIGHT')
        elif grid[x][y+1] == 'g' or grid[x][y+1] == 'r' or grid[x][y+1] == '#':
            if (grid[x-1][y] == '-'):
                print('UP')
            elif grid[x-1][y] == 'g' or grid[x-1][y] == 'r' or grid[x-1][y] == '#':
                if (grid[x][y-1] == '-'):
                    print('LEFT')
                elif grid[x][y-1] == 'g' or grid[x][y-1] == 'r' or grid[x][y-1] == '#':
                    print('DOWN')
                
    
def main():
    player1 = input()

    current_pos_parts = input().split(' ')

    player1_pos = (current_pos_parts[0],current_pos_parts[1])
    player2_pos = (current_pos_parts[2],current_pos_parts[3])

    grid = [[j for j in input().strip()] for i in range(15)]
    nextmove(grid, player1_pos, player2_pos)

main()
