# Problem 9: Sudoku Solver (Hard)
# Write a program that solves a given 9x9 Sudoku puzzle using a backtracking algorithm.
# The input will be a partially filled grid (with empty cells represented by 0),
# and the output should be the completed board.
# Example:
#   Input: 9x9 grid with zeros for empty cells
#   Output: Fully solved 9x9 Sudoku board

def solve_sudoku(board):
    # TODO: Implement the backtracking algorithm to solve the Sudoku

# Example board (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Test
solved_board = solve_sudoku(sudoku_board)
for row in solved_board:
    print(row)
