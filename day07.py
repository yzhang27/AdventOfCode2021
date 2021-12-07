import math


def read_input(filename):

    with open(filename, 'r') as f:
        line = f.readline()
        positions = list(map(int, line.strip().split(',')))

    return positions


def leastFuelPosition(filename, by_one):

    positions = read_input(filename)
    min_position = min(positions)
    max_position = max(positions)
    min_fuel_used = float('inf')

    i = min_position
    while i <= max_position:
        fuel_used = 0
        for p in positions:
            if p != i:
                if by_one:
                    fuel_used += abs(p-i)
                else:
                    diff = abs(p-i)
                    fuel_used += (math.pow(diff, 2) + diff) / 2
        min_fuel_used = min(fuel_used, min_fuel_used)
        i += 1

    return min_fuel_used


input_file = 'puzzle_input/day07.txt'

print(leastFuelPosition(input_file, True))
print(leastFuelPosition(input_file, False))
