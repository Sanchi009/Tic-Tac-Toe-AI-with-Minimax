"""
Tic Tac Toe Player
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
    countx = 0
    counto = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == X:
                countx += 1
            elif board[row][col] == O:
                counto += 1

    return X if (countx == counto) else O 

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                action.add((row, col))
    return action

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action
    if row < 0 or row >= len(board)  or col < 0 or col >= len(board[0]):
        raise IndexError()
    
    b = [x[:] for x in board] 
    b[row][col] = player(board)
    return b

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if hor(board, X) or ver(board, X)  or leftd(board, X) or rightd(board, X):
        return X
    elif hor(board, O) or ver(board, O) or leftd(board, O) or rightd(board, O):
        return O
    else:
        return None
    
def hor(board, player):
    for row in range(3):
        count = 0
        for col in range(3):
            if board[row][col] == player:
                count += 1
        if count == 3:
            return True
    return False
      
def ver(board, player):
    for col in range(3):
        count = 0
        for row in range(3):
            if board[row][col] == player:
                count += 1
        if count == 3:
            return True
    return False
        
      
def leftd(board, player):
    count = 0
    for row in range(3):
        for col in range(3):
            if(row == col and board[row][col] == player):
                count += 1 
    return count == len(board)
        
        
def rightd(board, player):
    count = 0
    for row in range(3):
        for col in range(3):
            if(row == len(board) - col - 1 and board[row][col] == player):
                count += 1
    return count == len(board)
     
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True

    for row in range(len(board)):
        for col in range(len(board[0])):
            if(board[row][col] == EMPTY):
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0 



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        arr = []
        for action in actions(board):
            arr.append([minvalue(result(board, action)), action])
        return sorted(arr, key=lambda x : x[0], reverse=True)[0][1]
    elif player(board) == O:
        arr = []
        for action in actions(board):
            arr.append([maxvalue(result(board, action)), action])
        return sorted(arr, key=lambda x : x[0])[0][1]

def maxvalue(board):
    if terminal(board):
        return utility(board)
    val = float("-inf")
    for action in actions(board):
        val = max(val, minvalue(result(board, action)))
    return val

def minvalue(board):
    if terminal(board):
        return utility(board)
    val = float("inf")
    for action in actions(board):
        val = min(val, maxvalue(result(board, action)))
    return val