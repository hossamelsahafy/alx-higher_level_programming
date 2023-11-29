#!/usr/bin/python3
import sys


def print_board(board):
    """print the board"""
    print([[col for col in row] for row in board])


def is_safe(board, row, col):
    """check if a position is safe"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nq(board, col):
    """solve the n queens problem"""
    if col >= len(board):
        print_board(board)
        print("\n")
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            solve_nq(board, col + 1)
            board[i][col] = 0
    return False


def solve(N):
    """create the board and start solving"""
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nq(board, 0):
        print("Solution does not exist")
        return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(N)
