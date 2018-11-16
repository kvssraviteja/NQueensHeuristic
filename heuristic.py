import random

def heuristic_free_cells(queens, n):

    board = create_board(queens, n)
    #print(board)
    for (x, y) in queens:

        for i in range(n):
            board[i][y] = 1
            board[x][i] = 1

        for i in range(min(x, n - 1 - y) + 1):
            board[x - i][y + i] = 1

        for i in range(min(x, y) + 1):
            board[x - i][y - i] = 1

        for i in range(min(n - 1 - x, n - 1 - y) + 1):
            board[x + i][y + i] = 1

        for i in range(min(n - 1 - x, y) + 1):
            board[x + i][y - i] = 1

    return sum(map(sum, board))


def heuristic_attcked_cells(queens, n):

    return n*n - heuristic_free_cells(queens, n)


def no_heuristic(queens, n):
    return 0


def heuristic_random(queens, n):
    return random.random()


def create_board(queens, n):

    board = [[0 for x in range(n)] for x in range(n)]
    for (i, j) in queens:
        board[i][j] = 1

    return board


