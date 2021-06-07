"""
Tic Tac Toe Player (assignment from cs50 course)
Author: Tyrel Cadogan 
email: shaqc777@yahoo.com
Github: https://github.com/T-rex007
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


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
    
    if(((x_times%2) ==1) or ((x_times%2) == 0)):
        return X
    else:
        return O

       

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for row in range(len(board)):
        for columns in range(len(board[0])):
            if(board[row][columns] == EMPTY):
                action_set.add(row,column)
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

    for column in range(0,len(board[0])):
        if(column == 0):
            ### Check all three possibilities at this position
            col = [board[i][i]  for i in range(len(board[0]))]
            if(all(elem == X for elem in board[0][:]) or all(elem == O for elem in board[0][:])):
                return X*all(elem == X for elem in board[0][:]) + O*all(elem == O for elem in board[0][:])

            elif(all(elem == X for elem in board[:][0]) or all(elem == O for elem in board[:][0])):
                return X*all(elem == X for elem in board[:][0]) + O*all(elem == O for elem in board[:][0])

            elif(all(elem == X for elem in col) or all(elem == O for elem in col)):
                ## check lead diagonal
                return X*all(elem == X for elem in col) + O*all(elem == O for elem in col)

        elif(column ==len(board[0])):
            col = [board[i][len(board[0])-1 -i]  for i in range(len(board[0]))]
            if(all(elem == X for elem in col) or all(elem == O for elem in col)):
                return X*all(elem == X for elem in col) + O*all(elem == O for elem in col)
        else:
            if(all(elem == X for elem in board[0][column]) or all(elem == O for elem in board[0][column])):
                return X*all(elem == X for elem in board[0][column]) + O*all(elem == O for elem in board[0][column])

    for row in range(1, len(board[0])):
        if(all(elem == X for elem in board[row]) or all(elem == O for elem in board[row])):
            return X*all(elem == X for elem in board[row]) + O*all(elem == O for elem in board[row])

    return None



    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board)
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board) == X):
        return 1
    elif(winner(board) == O):
        return -1
    return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
