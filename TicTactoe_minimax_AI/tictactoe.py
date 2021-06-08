"""
Tic Tac Toe Player (assignment from cs50 course)
Author: Tyrel Cadogan 
email: shaqc777@yahoo.com
Github: https://github.com/T-rex007
"""

import math
import numpy as np
import sys

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return np.array([[EMPTY, EMPTY, EMPTY],
                     [EMPTY, EMPTY, EMPTY],
                     [EMPTY, EMPTY, EMPTY]])


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_times = 0
    o_times = 0

    for row in range(len(board)):
        for columns in range(len(board[0])):
            if(board[row][columns] == X):
                x_times += 1
            elif(board[row][columns] == O):
                o_times += 1
    
    if( (((x_times+o_times)%2) == 0)):
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for row in range(len(board)):
        for column in range(len(board[0])):
            if(board[row][column] == EMPTY):
                action_set.add((row,column))
    return action_set

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]]= player(board)
    
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """ 
    # Check the two edge cases (the diagonals)
    
    d1 = [board[i][i] for i in range(len(board[0]))]
    win_check_x = all(elem == X for elem in d1)
    win_check_O = all(elem == O for elem in d1)
    if(win_check_x or win_check_O):
        return X *win_check_x + O*win_check_O

    d2 = [board[i][len(board)-1 -i] for i in range(len(board[0]))]
    win_check_x = all(elem == X for elem in d2)
    win_check_O = all(elem == O for elem in d2)
    if(win_check_x or win_check_O):
        return X *win_check_x + O*win_check_O
    
    for column in range(len(board[0])):
        win_check_x = all(elem == X for elem in board[:, column])
        win_check_O = all(elem == O for elem in board[:, column])
        if(win_check_x or win_check_O):
            return X *win_check_x + O*win_check_O

    for row in range(len(board[0])):
        win_check_x = all(elem == X for elem in board[row, :])
        win_check_O = all(elem == O for elem in board[row, :])
        if(win_check_x or win_check_O):
            return X *win_check_x + O*win_check_O

    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if((winner(board) == X) or (winner(board) == O)):
        return True
    else:
        return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board) == X):
        return 1
    elif(winner(board) == O):
        return -1
    return 0

def max_value(board):
    """
    Returns the action with the largest value of min_value 
    """
    if terminal(board):
        return utility(board)
    # Lowest possible number
    v = -sys.maxint
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    """
    Returns the smallest value that produces the smallest value of max_value
    """
    if terminal(board):
        return utility
    v = sys.maxint
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(player(board) == X):
        return max_value
    elif(player(board) == O):
        return min_value
    else:
        raise ValueError


if __name__ == "__main__":
    board = initial_state()
    print("Player: ",player(board))
    print("Actions: ",actions(board))
    print("Wineer: ",winner(board))