# Tic-Tac-Toe with Minimax and Pygame 🧩
This project is a Tic-Tac-Toe game where you can play against an AI powered by the Minimax algorithm. It includes a graphical user interface (GUI) built with Pygame, making the game more interactive and visually appealing. 

## Features 💎
- **Minimax Algorithm**: The AI uses the Minimax algorithm, which evaluates all possible moves and chooses the optimal one. It ensures the AI plays perfectly.
- **Graphical UI with Pygame**: The game utilizes Pygame to render an intuitive and visually attractive interface, including buttons, game board, and animations for 'X' and 'O'.

## Algorithm Overview 🐍
The Minimax algorithm is a recursive method used to decide the next best move. The AI (playing as 'X' or 'O') tries to maximize its chances of winning, while minimizing the opponent's. Here's how the algorithm works:

1. **Maximizing Player**: When it's the AI's turn, it tries to maximize its score.
2. **Minimizing Player**: The human player tries to minimize the AI's score.
3. **Game State Evaluation**: The utility function assigns a score of +1 for an AI win, -1 for a human win, and 0 for a draw.

The algorithm evaluates every possible move and selects the one that leads to the best outcome.

## Pygame Integration 🕹️
Pygame is used to build the GUI, rendering the game board, symbols, and handling user input. It updates the game state and draws each move, making the game visually engaging.

- The game board is a 3x3 grid, drawn using Pygame's line functions.
- The player's and AI's moves are drawn as 'X' and 'O' using custom shapes (lines for 'X' and circles for 'O').
- The user selects their symbol ('X' or 'O') and plays by clicking on the grid.

## Installation & Setup 💻

1. **Clone the repository**: 
   
   ```bash
   git clone https://github.com/Mecha-Aima/AI-powered-TicTacToe.git
   
2. **Install PyGame**:

   You can install Pygame via pip:
   ```bash
   pip install pygame

3. **Run the Game**:

  Once Pygame is installed, run the game:
  ```bash
  python game.py
```

## How the GUI Renders the Logic 🖌️
* **Game Board:** \
  The 3x3 grid is drawn using Pygame’s line function. Empty cells are detected, and moves are rendered as 'X' or 'O' using Pygame’s draw functions (lines for 'X' and circles for 'O').
  
* **User Interaction:** \
  The player clicks on the board to make a move. The game responds to mouse events, updates the state, and re-renders the board.
  
* **AI Turn:** \
  After each player move, the AI (Minimax) calculates its best move and updates the board.

---
This small project demonstrates a combination of game AI (Minimax) with a clean, interactive UI using Pygame. Enjoy playing against a strong AI! 🤖
