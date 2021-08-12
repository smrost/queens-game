import argparse

from board import Board
from queen import Queen

# https://en.wikipedia.org/wiki/Eight_queens_puzzle
def numberOfSolutions(i, board): #creates all possible solutions
    if (i < board.size()):
        queen = Queen()
        count = 0

        for j in range(board.size()):
            queen.placeOn(board, i, j)
            if (board.admissiblePlacementFor(queen)):
                count = count + numberOfSolutions(i + 1, board)
            queen.removeFromBoard()

        return count
    else:
        return 1

parser = argparse.ArgumentParser(description="Solve the Queen\'s puzzle of the specified size")
parser.add_argument('size', metavar='N', type=int,
                    help='an integer for the size of the board and number of queens')
args = parser.parse_args()

size = args.size
board = Board(size)

print(numberOfSolutions(2, board))