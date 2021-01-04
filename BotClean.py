#!/bin/python3
'''
A deterministic environment is one where the next state is completely determined by the current state of the environment and the task executed by the agent. If there is any randomness involved in determining the next state, the environment is stochastic.

The game Bot Clean took place in a deterministic environment. In this version, the bot is given 200 moves to clean as many dirty cells as possible. The grid initially has 1 dirty cell. When the bot cleans this cell, a new cell in the grid is made dirty. The new cell can be anywhere in the grid.

The bot here is positioned at the top left corner of a 5*5 grid. Your task is to move the bot to appropriate dirty cell and clean it.

Input Format
The first line contains two single spaced integers which indicates the current position of the bot. The grid is indexed (x, y) 0<=x,y<=4 top to bottom and left to right respectively. Refer to to board convention here.

5 lines follow showing the grid rows. Each cell in the grid is represented by any of the following 3 characters:

'b' (ascii value 98) - the bot's current position (if on clean cell).

'd' (ascii value 100) - a dirty cell (even if the robot is present on top of it).

'-' (ascii value 45) - a clean cell in the grid.
'''

def nextMove(posr, posc, board):
    location_row = 0
    location_col = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'd':
                location_row = i
                location_col = j
                
    if location_col > posc:
        print("RIGHT")
    elif location_col < posc:
        print("LEFT")
    elif location_row < posr:
        print("UP")
    elif location_row > posr:
        print("DOWN")
    else:
        print("CLEAN")
        
    
    
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
