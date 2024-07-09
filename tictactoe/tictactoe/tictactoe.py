"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None
WinCnt = 3


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
    Returns player who has the next turn on a board.

    Args:
        board (list): 2 dimension

    Raises:
        NotImplementedError: _description_

    Returns:
        Character: the player according to the board 
    """
    # first determine whether this board is a terminal state
    if terminal(board):
        return EMPTY    # if this is a terminal state ,return anything
    Xcnt = 0
    Ocnt = 0
    for row in board:
        for col in row:
            if col == X:
                Xcnt += 1
            if col == O:
                Ocnt += 1
            
    if Xcnt == Ocnt : return X
    else : return O
    
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return []
    availableActions = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                availableActions.append((row,col))
    return availableActions
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    play = player(board)
    i , j = action
    if board[i][j] != EMPTY:
        raise Exception(" infeasible move")
    new_board[i][j] = play
    return new_board
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win = utility(board)
    if win == 0:
        return None
    elif win == 1:
        return X
    else :
        return O
    
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    flag = False
    for row in board:
        for col in row:
            if col == EMPTY:
                flag = True
    
    if not flag: return True
    
    for row in board:
        if all(col == row[0] for col in row) and row[0] != EMPTY:
            return True
    transposed_board = [list(row) for row in zip(*board)]
    for row in transposed_board :
        if all(col == row[0] for col in row) and row[0] != EMPTY:
            return True
        
    diag = [board[0][0],board[1][1],board[2][2]]
    diag2 = [board[2][0],board[1][1],board[0][2]]
    if all(e == diag[0] for e in diag) and diag[0] != EMPTY:
        return True
    if all(e == diag2[0] for e in diag2) and diag2[0] != EMPTY:
        return True
    
    return False
    # raise NotImplementedError

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # determin every row 
    for row in board:
        if all(col == row[0] for col in row):
            if row[0] == X :
                return 1
            elif row[0] == O:
                return -1
            
    transposed_board = [list(row) for row in zip(*board)]
    for row in transposed_board:
        if all(col == row[0] for col in row):
            if row[0] == X :
                return 1
            elif row[0] == O:
                return -1
    
    # 考虑对角线 方向的内容
    diag = [board[0][0],board[1][1],board[2][2]]
    diag2 = [board[2][0],board[1][1],board[0][2]]
    if all(e == diag[0] for e in diag):
        if diag[0] == X:
            return 1
        elif diag[0] == O:
            return -1
    
    if all(e == diag2[0] for e in diag2):
        if diag2[0] == X:
            return 1
        elif diag2[0] == O:
            return -1
    
    return 0
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    def MaxValue(board):
        if terminal(board):
            return utility(board)
        
        val = -math.inf
        for action in actions(board):
            val = max(val,MinValue(result(board,action)))
        
        return val
    
    def MinValue(board):
        if terminal(board):
            return utility(board)
        
        val = math.inf
        for action in actions(board):
            val = min(val , MaxValue(result(board,action)))
        
        return val
    
    if terminal(board):
        raise Exception("minimax function receive a terminate state")
        # return utility(board)
    
    value = -math.inf
    chooseAction = None
    for action in actions(board):
        res = MinValue(result(board,action))
        if res > value:
            chooseAction = action
            value = res
    
    return chooseAction
        
            
    # raise NotImplementedError
