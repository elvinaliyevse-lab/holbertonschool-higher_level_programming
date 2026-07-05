#!/usr/bin/python3
"""Solve the N queens problem using backtracking."""
import sys


def solve(n):
    """Yield every solution as a list of [row, col] pairs."""
    cols = set()        # occupied columns
    diag1 = set()       # occupied "/" diagonals (row - col)
    diag2 = set()       # occupied "\" diagonals (row + col)
    board = []

    def backtrack(row):
        if row == n:
            yield [[r, c] for r, c in enumerate(board)]
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board.append(col)
            yield from backtrack(row + 1)
            board.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    yield from backtrack(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for solution in solve(n):
        print(solution)
