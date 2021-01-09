'''
Author: shamo0

MegaMaid is a robot whose function is to move through a matrix and 
clean all of its dirty cells. It's positioned in some cell of an 
h x w matrix of dirty (d) and clean (-) cells. It can perform five 
types of operations:

LEFT: Move one cell to the left.
RIGHT: Move one cell to the right.
UP: Move one cell up.
DOWN: Move one cell down.
CLEAN: Clean the cell.

Given the robot's current location and the configuration of dirty 
and clean cells in the matrix, print the next operation MegaMaid 
will perform (e.g., UP, CLEAN, etc.) on a new line.
'''
def next_move(posr, posc, dimx, dimy, board):

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
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
