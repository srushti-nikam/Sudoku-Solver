N = 9

def isSafe(sudoku, row, col, num):
    for i in range(9):
        # To check if there is same num in a particular row
        if sudoku[row][i] == num:
            return False

    for i in range(9):
        # To check if there is same num in a particular column
        if sudoku[i][col] == num:
            return False

    # To check if same num exists in 3x3 grid
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[startRow + i][startCol + j] == num:
                return False
    return True

# creating function to assign values to all non-assigned locations
def solveSudoku(sudoku, row, col):
    if row == N - 1 and col == N:     # base condition since using recursion
        return True

    if col == N:
        row += 1
        col = 0

    if sudoku[row][col] > 0:
        return solveSudoku(sudoku, row, col + 1)

    for num in range(1, N + 1):
        if isSafe(sudoku, row, col, num):
            sudoku[row][col] = num

            # checking possibility for next column
            if solveSudoku(sudoku, row, col + 1):
                return True

        sudoku[row][col] = 0
    return False


def solver(sudoku):
    # To check if sudoku is solvable starting from 0th row and 0th column
    if solveSudoku(sudoku, 0, 0):
        return sudoku
    else:
        print("No solution exists for this sudoku")
        return "no"


def solver(sudoku):
    # To check if sudoku is solvable starting from 0th row and 0th column
    if solveSudoku(sudoku, 0, 0):
        return sudoku
    else:
        print("No solution exists for this sudoku")
        return "no"