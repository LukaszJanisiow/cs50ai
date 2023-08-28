"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY,EMPTY]]


def player(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                count += 1
            elif board[i][j] == O:
                count -= 1
    return X if count == 0 else O


def actions(board):
    ans = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                ans.add((i,j))
    return ans


def result(board, action):
    ans = copy.deepcopy(board)
    if ans[action[0]][action[1]] == EMPTY:
        ans[action[0]][action[1]] = X if player(board) == X else O
    else:
        raise NameError('Errorrrrrr')
    return ans

def winner(board):
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    for i in range(3):
        temp = True
        for j in range(1,3):
            if board[j][i] != board[0][i]:
                temp = False
                break
        if temp:
            return board[0][i]
    return None


def terminal(board):
    if winner(board):
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    temp = winner(board)
    if temp == X:
        return 1
    elif temp == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None
    actplayer = player(board)
    score = float('-inf') if actplayer == X else float('inf')
    optimal_action = None
    for action in actions(board):
        temp = helper(result(board,action))
        if actplayer == X and temp > score:
            score = temp
            optimal_action = action
        elif actplayer == O and temp < score:
            score = temp
            optimal_action = action
    return optimal_action
    

def helper(board):
    if terminal(board):
        return utility(board)
    actplayer = player(board)
    score = float('-inf') if actplayer == X else float('inf')
    for action in actions(board):
        temp = helper(result(board,action))
        if actplayer == X and temp > score:
            score = temp
        elif actplayer == O and temp < score:
            score = temp
    return score

