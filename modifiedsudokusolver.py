# Modified version
# A Backtracking program
# in Python to solve Sudoku problem

# sudoku = input("Enter Soduku: ")
# # 070000009510420600080300700008001370023080040400900100962800030000010400700203096
# board = [[int(sudoku[(i+j)-1]) for i in range(1,10)] for j in range(0,81,9)]
# print("List type:")
# print(board)

def check_modified(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def check(puzzle, i, row, col):
    rows = puzzle[int(row)]
    column = [puzzle[r][col] for r in range(0,9,1)]
    if i in rows:
        return False
    if i in column:
        return False
    SquareRow = (row // 3)*3
    squareColumn = (col // 3)*3
    Square = [puzzle[y][z] for y in range(SquareRow, SquareRow+3) for z in range(squareColumn, squareColumn+3)]
    if i in Square:
        return False
    return True


def find(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j]==0:
                return i,j
    return None


def solve(board):
    finds = find(board)
    if not finds:
        return True
    else:
        row, col = finds

    for i in range(1,10):
        if check(board, i, row, col):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

# print("\nUnsolved Sudoku Problem:")
# print_board(board)
# solve(board)
# print("\n_________________________\n")
# print("Solved Sudoku Problem:")
# print_board(board)