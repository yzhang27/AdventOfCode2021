def read_input(filename):
    moves = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            direction, steps = line.rstrip().split(' ')
            line = f.readline()
            moves.append((direction, int(steps)))

    return moves


def calcPosition(filename):

    moves = read_input(filename)
    horizontal, depth = 0, 0

    for direction, steps in moves:
        if direction == 'forward':
            horizontal += steps
        elif direction == 'up':
            depth -= steps
        elif direction == 'down':
            depth += steps

    return horizontal*depth


def calcPositionWithAim(filename):

    moves = read_input(filename)
    horizontal, depth, aim = 0, 0, 0

    for direction, steps in moves:
        if direction == 'forward':
            horizontal += steps
            depth += steps * aim
        elif direction == 'up':
            aim -= steps
        elif direction == 'down':
            aim += steps

    return horizontal*depth


input_file = 'puzzle_input/day02.txt'
print(calcPosition(input_file))
print(calcPositionWithAim(input_file))
