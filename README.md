# Fourtic Game Solver

The Fourtic Game Solver is a Python program designed to solve a variant of the classic Tic-Tac-Toe game, where the board is a 4x4 grid and scoring is based on a new set of rules defined below. This program features a Negamax Depth Search algorithm capable of assesing the board and returning the current player and their position value.

## Modules and Constants

- `sys`: Module used to handle command-line arguments.
- `FILENAME`: Default file containing the game board state.
- `N`: Size of the game board (4x4).

## Testing

- `TESTS`: Boolean flag to run tests using predefined board states from files.
- `RAND_FILES` and `PLAY_FILES`: Tuples containing file names, expected player's turn, and expected outcome score for test cases.

## Main Function

The `main()` function is the entry point of the program. It:

- Handles command-line input or uses a default input file.
- Runs tests if the `TESTS` flag is true.
- Executes a single run of the Negamax solver on the provided game board.

## Fourtic Class

The `Fourtic` class encapsulates the game logic and solver. Its methods include:

- `__init__(self, board=None)`: Constructor initializing the board.
- `printBoard(self)`: Prints the board in a readable format.
- `clearBoard(self)`: Clears the game board for a new game.
- `getTurn(self)`: Assesses the board and returns whose turn it is and the piece count.
- `getScore(self, piece)`: Analyzes the board and returns the score based on the current pieces' positions.
- `getMoves(self)`: Returns a list of possible moves for the current turn.
- `makeMove(self, newMove, piece)`: Makes a move on the board.
- `gameOver(self)`: Checks if the game is over.
- `negamax(self, depth=16)`: Runs the Negamax algorithm to determine the best move for the current player.

## Helper Function

- `read_board(filename)`: Reads the board state from a file and returns it as a 2D list.

## Building and Usage

### Requirements

Ensure you have Python installed on your system.

### Setup

1. Clone the repository or download the source code to your local machine.
2. Place any `.txt` files representing game boards in the same directory as the script.

### To use the solver:

1. Run the program with the file as an argument: `python fourtic_solver.py board.txt`
2. The program will print the result in the format `Player, Score`.

## Fourtic Game Rules Summary

Created by Bart Massey, Fourtic is a quick, strategic 4x4 grid game for two players, each taking turns marking the cells with X or O, starting with X.

### Gameplay

- Players alternate placing Xs and Os on the board.
- The game ends when all cells are filled, with each player making eight moves.

### Scoring

- A row of three identical symbols scores 3 points.
- Each occupied corner or side square scores 1 point.

### Winning

The player with the most points when the board is full wins the game.

### Example Board File

A board file should look like this:

X...

.O..

..X.

...O

Each line represents a row on the board, and each character represents a cell, where `.` is an empty cell, `X` is a cell occupied by player X, and `O` is a cell occupied by player O.
