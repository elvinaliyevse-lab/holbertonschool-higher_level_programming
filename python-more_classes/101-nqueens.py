#!/usr/bin/python3
"""Module solving Nqueens problem"""
import sys


def main():
    """Main function"""

    # Checking if usage is correct
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Checking if value specified is int
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Checking if board is at least 4 x 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Breaking the problem
    solutions = nqueens(N)

    # Printing the solutions
    for solution in solutions:
        print(solution)


def nqueens(N):
    """Primary function"""

    # Creating the board
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    # Placing the queens
    place_queens(board, 0, N, solutions)
    return solutions


def place_queens(board, col, N, solutions):
    """Function for placing the queens in board"""
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(N):
        if is_position_safe(board, i, col, N):
            board[i][col] = 1
            place_queens(board, col + 1, N, solutions)
            board[i][col] = 0


def is_position_safe(board, row, col, N):
    """Function to check if position is safe in board"""
    # Check this column on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


if __name__ == "__main__":
    """Instantiation of code"""
    main()
