import pygame
import sys
import time
from tictactoe_minmax import *

WIDTH, HEIGHT = (800, 800)
# Colors
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)
LIGHT_YELLOW = (255, 255, 180)
BLACK = (0, 0, 0)

def choose_symbol(screen):
    """
    Displays a screen for the user to choose their symbol ('X' or 'O').
    
    Parameters:
    screen (pygame.Surface): The pygame surface where the symbols and UI elements are drawn.
    
    Returns:
    str: The symbol chosen by the user ('X' or 'O').
    """
    # Set up font and label for the title
    font = pygame.font.Font('RG-SpaciousBook.ttf', 32)
    label = font.render("Choose your symbol", True, LIGHT_YELLOW)
    label_rect = label.get_rect(center=(WIDTH // 2, 120))

    # Define dimensions and positions for the buttons
    button_width = 150
    button_height = 50
    button_x = (WIDTH - 2 * button_width) // 3
    button_y = 200
    button_x2 = button_x + button_width + button_x

    # Create rectangles for the 'X' and 'O' buttons
    button_x_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    button_o_rect = pygame.Rect(button_x2, button_y, button_width, button_height)

    while True:
        # Fill screen with black and draw the title label
        screen.fill(BLACK)
        screen.blit(label, label_rect)

        # Draw the 'X' and 'O' buttons
        pygame.draw.rect(screen, LIGHT_BLUE, button_x_rect)
        pygame.draw.rect(screen, LIGHT_GREEN, button_o_rect)

        # Render and position text labels for the buttons
        button_x_label = font.render('X', True, BLACK)
        button_o_label = font.render('O', True, BLACK)
        screen.blit(button_x_label, (button_x_rect.center[0] - button_x_label.get_width() // 2, button_x_rect.center[1] - button_x_label.get_height() // 2))
        screen.blit(button_o_label, (button_o_rect.center[0] - button_o_label.get_width() // 2, button_o_rect.center[1] - button_o_label.get_height() // 2))

        # Update the display
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for mouse button click on the 'X' or 'O' button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_x_rect.collidepoint(event.pos):
                    return 'X'
                elif button_o_rect.collidepoint(event.pos):
                    return 'O'

def game():
    """
    Main game loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tic-Tac-Toe')
    font = pygame.font.Font('RG-SpaciousBook.ttf', 32)

    user_symbol = choose_symbol(screen)
    computer_symbol = 'X' if user_symbol == 'O' else 'O'
    user_player = 1 if user_symbol == 'X' else -1
    computer_player = -user_player

    current_state = copy.deepcopy(board)
    current_player = user_player
    turn = "Your Turn"

    screen.fill(BLACK)
    turn_label = font.render(turn, True, LIGHT_YELLOW)
    turn_label_rect = turn_label.get_rect(center=(WIDTH // 2, 50))
    screen.blit(turn_label, turn_label_rect)
    draw_board(screen, current_state)
    pygame.display.flip()

    running = True
    while running and not terminal(current_state):
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen and draw the current state
        screen.fill(BLACK)
        turn_label = font.render(turn, True, LIGHT_YELLOW)
        turn_label_rect = turn_label.get_rect(center=(WIDTH // 2, 50))
        screen.blit(turn_label, turn_label_rect)
                
        if current_player == user_player:
            # User's turn
            turn= "Your Turn"
            action = get_user_action(current_state)
            current_state = result(current_state, (action, user_symbol))
        else:
            # Computer's turn
            turn = "Computer's Turn"
            time.sleep(1)
            _, action = minmax(computer_player, current_state)
            current_state = result(current_state, action)

        current_player = -current_player   
        
        draw_board(screen, current_state)
        pygame.display.flip()

    if running:
        time.sleep(1.5)
        winner = terminal(current_state)
        display_winner(screen, winner)

    pygame.quit()
    sys.exit()

GRID_SIZE = 3
CELL_SIZE = 150
LINE_WIDTH = 3

GRID_WIDTH = GRID_HEIGHT = GRID_SIZE * CELL_SIZE
offset_x = (WIDTH - GRID_WIDTH) // 2
offset_y = (HEIGHT - GRID_HEIGHT) // 2

def draw_grid(screen):
    for x in range(1,GRID_SIZE):
        # Vertical lines
        pygame.draw.line(surface=screen, color=WHITE, start_pos=(offset_x+ x*CELL_SIZE, offset_y), 
                         end_pos=(offset_x + x*CELL_SIZE, offset_y + GRID_HEIGHT), width=LINE_WIDTH)
        # Horizontal lines
        pygame.draw.line(surface=screen, color=WHITE, start_pos=(offset_x, offset_y + x * CELL_SIZE),
                         end_pos=(offset_x + GRID_WIDTH, offset_y + x * CELL_SIZE), width=LINE_WIDTH)
        
def draw_X(screen, x, y):
    padding = 20
    pygame.draw.line(surface=screen, color=LIGHT_BLUE, 
                     start_pos=(offset_x + x * CELL_SIZE + padding, offset_y + y * CELL_SIZE + padding), 
                     end_pos=(offset_x + (x + 1)*CELL_SIZE - padding, offset_y + (y + 1)*CELL_SIZE - padding),
                     width=LINE_WIDTH)
    pygame.draw.line(surface=screen, color=LIGHT_BLUE, 
                     start_pos=(offset_x + (x + 1)*CELL_SIZE - padding, offset_y + y * CELL_SIZE + padding), 
                     end_pos=(offset_x + x*CELL_SIZE + padding, offset_y + (y + 1)*CELL_SIZE - padding),
                     width=LINE_WIDTH)
    
def draw_O(screen, x, y):
    padding = 20
    center = (offset_x + x*CELL_SIZE + CELL_SIZE//2, offset_y + y*CELL_SIZE + CELL_SIZE//2)
    radius = CELL_SIZE // 2 - 20
    pygame.draw.circle(surface=screen, color=LIGHT_GREEN, center=center, radius=radius, width=LINE_WIDTH)

def draw_board(screen, board):
    """
    Draws the tic-tac-toe board on the given screen with the current state.

    Args:
        screen (pygame.Surface): The pygame surface where the board is drawn.
        board (list): A 2D list representing the current board state.
    """
    # Draw the grid lines
    draw_grid(screen)

    # Iterate over each cell in the board
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            # Draw 'X' if the cell contains 'X'
            if board[row][col] == 'X':
                draw_X(screen, col, row)
            # Draw 'O' if the cell contains 'O'
            elif board[row][col] == 'O':
                draw_O(screen, col, row)

def get_user_action(state):
    """
    Get the user's action (row and column) from a mouse click event.

    Args:
        state (list): A 2D list representing the current board state.

    Returns:
        tuple: A tuple containing the row and column of the user's action.
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Get the mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Calculate the grid row and col
                row = (mouse_y - offset_y) // CELL_SIZE
                col = (mouse_x - offset_x) // CELL_SIZE

                # Check if the user clicked on a valid cell
                if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                    # Check if the clicked cell is empty
                    if state[row][col] == 0:
                        return row, col
                    else:
                        print("Cell is already occupied. Try again.")

def display_winner(screen, winner):
    """
    Displays the winner of the game on the screen.

    Args:
        screen (pygame.Surface): The pygame surface to draw on.
        winner (str): The winner of the game ('X' or 'O').

    Returns:
        None
    """
    # Clear the screen
    screen.fill(BLACK)

    # Set up the font
    font = pygame.font.Font('RG-SpaciousBook.ttf', 40)

    # Draw the winner message
    if winner == 'X':
        # X wins
        pygame.draw.rect(screen, LIGHT_BLUE, (0, HEIGHT // 2 - 100, WIDTH, 200))
        label = font.render('X Wins!!!', True, BLACK)
    elif winner == 'O':
        # O wins
        pygame.draw.rect(screen, LIGHT_GREEN, (0, HEIGHT // 2 - 100, WIDTH, 200))
        label = font.render('O Wins!!!', True, BLACK)
    else:
        # Draw
        pygame.draw.rect(screen, WHITE, (0, HEIGHT // 2 - 100, WIDTH, 200))
        label = font.render("It's a DRAW", True, BLACK)

    # Center the label
    label_rect = label.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Draw the label
    screen.blit(label, label_rect)

    # Update the display
    pygame.display.flip()

    # Wait for the user to close the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == '__main__':
    game()


