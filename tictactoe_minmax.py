import copy

# Initialize the board
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def result(state, action) -> list:
    """
    Return the new state after the given action.

    Args:
        state (list): The current board state as a 2D list.
        action (tuple): A tuple containing the cell coordinates (i, j) and the player's symbol ('X' or 'O').

    Returns:
        list: The new board state as a 2D list.
    """
    r, c = action[0]
    if not valid_cell(r, c):
        raise ValueError("Invalid cell")
    symbol = action[1]
    new_state = copy.deepcopy(state)  # Create a new board state by copying the current one
    new_state[r][c] = symbol  # Update the cell with the player's symbol
    return new_state

def utility(player):
    """
    Return the score of the given player. 1 for 'X', -1 for 'O', and 0 for a draw.
    """
    if player == 'X':
        return 1
    elif player == 'O':
        return -1
    else:
        return 0

def actions(state, player):
    """
    Generate all possible actions for the given player in the current state.
    
    Args:
        state (list): The current board state as a 2D list.
        player (int): The player number, 1 for max player ('X'), -1 for min player ('O').
    
    Return:
        tuple: A tuple containing the cell coordinates (i, j) and the player's symbol ('X' or 'O').
    """
    if player == 1: # max player
        for cell in get_empty_cells(state):
            yield (cell, 'X')
    else: # min player
        for cell in get_empty_cells(state):
            yield (cell, 'O')


def get_empty_cells(state):
    """
    Generate all empty cells in the given state.
    
    Args:
        state (list): The current board state as a 2D list.
    
    Return:
        tuple: A tuple containing the empty cell coordinates (i, j).
    """
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                yield (i, j)

def valid_cell(r, c):
    # check if the cell is valid
    return r >= 0  and r < 3 and c >= 0 and c < 3

def terminal(state):
    """
    Check if the game has reached a terminal state.
    
    Args:
        state (list): The current board state as a 2D list.
    
    Return:
        int|str: The terminal value of the game, either the player that won (1 or -1), 'tie' if it's a draw, or False if it's not a terminal state yet.
    """
    # check rows
    for row in state:
        if row[0] == row[1] == row[2] and row[0] != 0:
            return row[0]
    # check columns
    for i in range(3):
        if state[0][i] == state[1][i] == state[2][i] and state[0][i] != 0:
            return state[0][i]
    # check diagonals
    if state[0][0] == state[1][1] == state[2][2] and state[0][0] != 0:
        return state[0][0]
    if state[0][2] == state[1][1] == state[2][0] and state[0][2] != 0:
        return state[0][2]
    
    # check if the board is full
    for row in state:
        for cell in row:
            if cell == 0:
                return False
    return 'tie'
    

def max_player(state):
    """
    Compute the best possible move for the max player in a given state.
    
    Args:
        state (list): The current board state as a 2D list.
    
    Return:
        tuple: A tuple containing the maximum possible value and the action that corresponds to that value.
    """
    if player := terminal(state):
        return utility(player), None
    max_value = float('-inf')
    best_action = None
    for action in actions(state, 1):
        v, _ = min_player(result(state, action))
        if v > max_value:
            max_value = v
            best_action = action
    
    return max_value, best_action

def min_player(state):
    """
    Compute the best possible move for the min player in a given state.
    
    Args:
        state (list): The current board state as a 2D list.
    
    Return:
        tuple: A tuple containing the minimum possible value and the action that corresponds to that value.
    """
    
    if player := terminal(state):
        return utility(player), None
    min_value = float('inf')
    best_action = None
    for action in actions(state, -1):
        v, _ = max_player(result(state, action))
        if v < min_value:
            min_value = v
            best_action = action

    return min_value, best_action

def minmax(player, state):
    """
    Compute the best possible move for the given player in a given state.

    Args:
        player (int): The player number, 1 for max player ('X'), -1 for min player ('O').
        state (list): The current board state as a 2D list.

    Return:
        tuple: A tuple containing the best possible value and the action that corresponds to that value.
    """
    if player == 1:
        return max_player(state)
    else:
        return min_player(state)