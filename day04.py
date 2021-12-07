import re
from collections import defaultdict


def read_input(filename):

    boards = []
    with open(filename, 'r') as f:

        numbers = list(map(int, f.readline().rstrip().split(',')))
        f.readline()
        board = []
        while line := f.readline():
            if line != '\n':
                board.append(list(map(int, re.split('[ ]+', line.strip()))))
            else:
                boards.append(board)
                board = []
        boards.append(board)

    return numbers, boards


def checkWinner(board, r, c):

    if board[r].count('x') == 5:
        return True

    for i in range(len(board)):
        if board[i][c] != 'x':
            return False

    return True


def bingo(filename, win_first):

    numbers, boards = read_input(filename)
    sums = defaultdict(int)
    board_sum = defaultdict(int)
    won_boards = []
    last_num = 0

    for i, board in enumerate(boards):
        for row in board:
            board_sum[i] += sum(row)

    for num in numbers:
        last_num = num
        for i, board in enumerate(boards):
            if i not in won_boards:
                for r, x in enumerate(board):
                    if num in x:
                        c = x.index(num)
                        sums[i] += board[r][c]
                        board[r][c] = 'x'
                        if checkWinner(board, r, c):
                            if win_first:
                                return (board_sum[i] - sums[i])*num
                            won_boards.append(i)

                if len(boards) == len(won_boards):
                    break
        if len(boards) == len(won_boards):
            break

    return (board_sum[i] - sums[i])*last_num


input_file = 'puzzle_input/day04.txt'
print(bingo(input_file, True))
print(bingo(input_file, False))
