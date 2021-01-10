#!/usr/bin/python
'''
Author: shamo0

The goal of Artificial Intelligence is to create a rational agent
(Artificial Intelligence 1.1.4). An agent gets input from the environment 
through sensors and acts on the environment with actuators. In this 
challenge, you will program a simple bot to perform the correct actions
based on environmental input.

Meet the bot MarkZoid. It's a cleaning bot whose sensor is a head mounted
camera and whose actuators are the wheels beneath it. It's used to clean
the floor.

The bot here is positioned at the top left corner of a 5*5 grid. Your 
task is to move the bot to clean all the dirty cells.
'''

def next_move(posr, posc, board):
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
    next_move(pos[0], pos[1], board)
