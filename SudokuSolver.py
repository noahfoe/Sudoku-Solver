board = [
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

def solve(bo):
    # recursive backtracking function
    find = find_empty(bo)
    # if we get to the end of the board, there is no need to verify that the solution is correct because of backtracking
    if not find:
        return True
    else:
        row, col = find
    # if valid, add to board
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            # recursive part
            if solve(bo):
                return True
            # reset and backtrack
            bo[row][col] = 0
    return False


def valid(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check col
    for i in range(0, 9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # label each box... top left is (0,0) and bottom right is (2,2)
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # check boxes
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

def print_board(bo):
    for i in range(0, 9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = " ")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end = " ")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, col
    return None

print("original")
print_board(board)
solve(board)
print(" ")
print("solution")
print_board(board)