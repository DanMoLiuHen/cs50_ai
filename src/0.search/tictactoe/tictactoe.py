"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    X_sum=sum([1 for row in board for cell in row if cell==X])
    O_sum=sum([1 for row in board for cell in row if cell ==O])

    return O if X_sum>O_sum else X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res=set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==EMPTY:
                res.add((i,j))
    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    try:
        new_board=deepcopy(board)
        user=player(board)
        row, col = action
        new_board[row][col]=user
        # print(new_board)
        return new_board
    except:
        print("[ERROR]")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if len(set(row))==1 and row[0]!=EMPTY:
            return X if row[0]==X else O
    for col in range(3):
        if len(set([board[i][col] for i in range(3)]))==1 and board[0][col]!=EMPTY:
            return X if board[0][col]==X else O
    if len(set([board[i][i] for i in range(3)]))==1 and board[0][0]!=EMPTY:
        return X if board[0][0]==X else O
    if len(set([board[i][2-i] for i in range(3)]))==1 and board[0][2]!=EMPTY:
        return X if board[0][2]==X else O
    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) !=None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for row in board:
        if len(set(row))==1 and row[0]!=EMPTY:
            return 1 if row[0]==X else -1
    for col in range(3):
        if len(set([board[i][col] for i in range(3)]))==1 and board[0][col]!=EMPTY:
            return 1 if board[0][col]==X else -1
    if len(set([board[i][i] for i in range(3)]))==1 and board[0][0]!=EMPTY:
        return 1 if board[0][0]==X else -1
    if len(set([board[i][2-i] for i in range(3)]))==1 and board[0][2]!=EMPTY:
        return 1 if board[0][2]==X else -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        move=()
        if terminal(board=board):
            return utility(board=board),move
        else:
            v=-9
            for action in actions(board=board):
                min=min_value(result(board=board,action=action))[0]
                if min>v:
                    v=min
                    move=action
            return v,move
                

    def min_value(board):
        move=()
        if terminal(board):
            return utility(board),move
        else:
            v=9
            for action in actions(board):
                max=max_value(result(board,action))[0]
                if max<v:
                    v=max
                    move=action
            return v,move
        
    cur=player(board)
    if terminal(board):
        return None
    return max_value(board)[1] if cur==X else min_value(board)[1]


    
