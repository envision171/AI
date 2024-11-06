def is_safe(board, row, col, n):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i] == j:
            return False

    return True


def solve_n_queens(board, row, n, solutions):
    # Base case: if all queens are placed
    if row == n:
        solutions.append(board[:])  # Append a copy of the solution
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # Place queen at (row, col)
            solve_n_queens(board, row + 1, n, solutions)  # Recurse to place next queen
            board[row] = -1  # Backtrack


# Main function to solve N-Queens
def n_queens(n):
    board = [-1] * n  # Initialize board with -1 (no queens placed)
    solutions = []  # To store all solutions
    solve_n_queens(board, 0, n, solutions)
    return solutions


# Display the solutions in a readable format
def print_solutions(solutions, n):
    for solution in solutions:
        for i in range(n):
            row = ['.'] * n
            row[solution[i]] = 'Q'
            print(" ".join(row))
        print("\n" + "-" * (2 * n - 1) + "\n")


# Example usage for N-Queens
n = int(input("Enter the value of N for the N-Queens problem: "))
solutions = n_queens(n)
print(f"\nNumber of solutions: {len(solutions)}\n")
print_solutions(solutions, n)
