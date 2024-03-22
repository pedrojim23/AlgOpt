def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty_location(board, l):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

def used_in_row(board, row, num):
    for i in range(9):
        if board[row][i] == num:
            return True
    return False

def used_in_col(board, col, num):
    for i in range(9):
        if board[i][col] == num:
            return True
    return False

def used_in_box(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if board[i + row][j + col] == num:
                return True
    return False

def is_safe_location(board, row, col, num):
    return not used_in_row(board, row, num) and not used_in_col(board, col, num) and not used_in_box(board, row - row % 3, col - col % 3, num)

def solve_sudoku(board):
    l = [0, 0]

    if not find_empty_location(board, l):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):
        if is_safe_location(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

if __name__ == "__main__":
    board = [[0 for j in range(9)] for i in range(9)]
    # Ingresa el sudoku como una lista de listas, donde los espacios vacíos se representan con 0
    sudoku = [
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
    for i in range(9):
        for j in range(9):
            board[i][j] = sudoku[i][j]
    if solve_sudoku(board):
        print("Sudoku resuelto:")
        print_board(board)
    else:
        print("No hay solución posible para este sudoku.")

