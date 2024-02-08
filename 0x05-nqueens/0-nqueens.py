#!/usr/bin/python3
'''N queen challenge'''
import sys


def is_safe(board, row, col, N):
    '''Check if there is a queen in the same column
       Auguments
          board: chess board(array)
          row: row in chess board
          col: column in chess board
          N: is a queen
       Return
          False: if there is a queen in a file
    '''
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    '''Placing queens on the board'''
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]

    def solve(board, row, N):
        '''printing the board with queens'''
        if row >= N:
            print_solution(board)
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve(board, row + 1, N)
                board[row][col] = 0

    solve(board, 0, N)


def print_solution(board):
    '''Printing the solution'''
    solution = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
