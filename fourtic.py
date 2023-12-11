import sys

# Constants
FILENAME = "play-3.txt"
N = 4

### TESTING ###
TESTS = False # Set true to run all tests through negamax solver
RAND_FILES = [("rand-2.txt", 'X', 3), ("rand-3.txt", 'O', 0), ("rand-4.txt", 'X', 3), ("rand-5.txt", 'O', 0), ("rand-6.txt", 'X', 0), ("rand-7.txt", 'O', 1)]
PLAY_FILES = [("play-2.txt", 'X', 3), ("play-3.txt", 'O', -3), ("play-4.txt", 'X', 3), ("play-5.txt", 'O', 0), ("play-6.txt", 'X', 4), ("play-7.txt", 'O', -2)]
###############

def main():
    # Handle Command Line input and default input
    filename = ""
    numArgs = len(sys.argv)
    if numArgs < 2:
        filename = FILENAME
    else:
        filename = sys.argv[1]

    # Testing File Results
    if TESTS:
        for group in RAND_FILES + PLAY_FILES:
            board = read_board(group[0])
            solver = fourtic(board)
            turn = solver.getTurn()[0][0]
            res = solver.negamax(8)
            print(group[0])
            print(turn, group[1])
            print(res, group[2])
            assert turn == group[1]
            assert res == group[2]
            
    # Individual Runs 
    else:
        board = read_board(filename)
        solver = fourtic(board)
        turn = solver.getTurn()[0][0]
        res = solver.negamax()
    
        print(turn, res)
        
    return


# Fourtic Class Object
class fourtic(object):
    def __init__(self, board=None):
        self.board = board
        assert board != None
    
    # Print the board in readable format
    def printBoard(self):
        for row in self.board:
            print(row)
    
    # Clear the board
    def clearBoard(self):
        for row in self.board:
            for col in self.board:
                self.board[row][col] = '.'
            
    # Assess the board and return the turn order as well as the piece count
    def getTurn(self):
        xCount = 0
        oCount = 0
        for row in range(N):
            for col in range(N):
                piece = self.board[row][col]
                if piece == 'X':
                    xCount += 1
                elif piece == 'O':
                    oCount += 1
        return ('X', 'O') if oCount >= xCount else ('O', 'X'), oCount + xCount
    
    # Analyze the board given a piece and return the respective score
    def getScore(self, piece):
        score = 0
        # Edge scores
        for row, col in [(0, 0), (0, 1), (0, 2), (0, 3), (3, 0), (3, 1), (3, 2), (3, 3), (1, 0), (2, 0), (1, 3), (2, 3)]:
            if self.board[row][col] == piece:
                score += 1
        # Horizontal 3 in a row
        for row, col in [(0,0), (0,1), (0,2), (0,3), (1, 0), (1, 1), (1, 2), (1, 3)]:
            if self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == piece:
                score += 3
        # Vertical 3 in a row
        for row, col in [(0,0), (0,1), (1,0), (1,1), (2, 0), (2, 1), (3, 0), (3, 1)]:
            if self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == piece:
                score += 3
        # Diagonal downward left to right
        for row, col in [(0,0), (0,1), (1,0), (1,1)]:
            if self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == piece:
                score += 3
        # Diagonal downward right to left
        for row, col in [(0,3), (0,2), (1,3), (1,2)]:
            if self.board[row][col] == self.board[row + 1][col - 1] == self.board[row + 2][col - 2] == piece:
                score += 3
        return score
    
    # Return a list of possible moves on this turn
    def getMoves(self):
        moves = []
        for row in range(N):
            for col in range(N):
                piece = self.board[row][col]
                # If the space is open add the move
                if piece == '.':
                    moves.append((row, col))
        return moves
    
    # Given a move and piece, alter the board
    def makeMove(self, newMove, piece):
        self.board[newMove[0]][newMove[1]] = piece
        return newMove
     
    # Check if the game is over
    def gameOver(self):
        for row in range(N):
            for col in range(N):
                # If any piece is . then there is still moves to be made
                if self.board[row][col] == '.':
                    return False
        return True
    
    # Negamax depth search to find the position value of the current player
    def negamax(self, depth=16):
        # Get current piece for player and opponent
        plr = self.getTurn()[0][0]
        opp = self.getTurn()[0][1]
        
        # If over return the score
        if self.gameOver() or depth == 0:
            return self.getScore(plr) - self.getScore(opp)
        
        max_value = -float('inf')
        moves = self.getMoves()
        # For every possible move
        for move in moves:
            # Make the move
            moveMade = self.makeMove(move, plr)
            # Recursive call, negative because opponent score is opposite
            value = -self.negamax(depth - 1)
            # Undo move
            self.makeMove(moveMade, '.')
            # Check for new max value
            max_value = max(max_value, value)
            
        return max_value
                
# Read in a file containing a board and return it as a 2D matrix                
def read_board(filename):
    boardFile = open(filename, 'r')
    board = []
    for row in boardFile:
        piece = [str(i) for i in row.removesuffix('\n')]
        board.append(piece)
    return board

# Run Program
main()