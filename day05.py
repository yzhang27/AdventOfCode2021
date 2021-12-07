from collections import defaultdict


def solution(file_name, diagonals):

    points = defaultdict(int)
    at_least_two = set()

    with open(file_name, 'r') as f:

        while line := f.readline():
            start, end = line.strip().split(' -> ')
            x1, y1 = list(map(int, start.split(',')))
            x2, y2 = list(map(int, end.split(',')))
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            if x1 == x2:
                for i in range(min_y, max_y+1):
                    point = f'{x1},{i}'
                    if point not in at_least_two:
                        points[point] += 1
                        if points[point] == 2:
                            at_least_two.add(point)
            elif y1 == y2:
                for i in range(min_x, max_x+1):
                    point = f'{i},{y1}'
                    if point not in at_least_two:
                        points[point] += 1
                        if points[point] == 2:
                            at_least_two.add(point)
            if diagonals:
                i = x1
                j = y1
                while max_x >= i >= min_x and max_y >= j >= min_y:
                    point = f'{i},{j}'
                    if point not in at_least_two:
                        points[point] += 1
                        if points[point] == 2:
                            at_least_two.add(point)
                    if x1 < x2:
                        i += 1
                    else:
                        i -= 1
                    if y1 < y2:
                        j += 1
                    else:
                        j -= 1

    return len(at_least_two)


input_file = 'puzzle_input/day05.txt'
print(solution(input_file, False))
print(solution(input_file, True))
