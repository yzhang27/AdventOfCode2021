def read_input(filename):
    measurements = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            measurements.append(int(line))
            line = f.readline()

    return measurements


def countIncreased(filename):
    count = 0
    measurements = read_input(filename)

    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            count += 1

    return count


def countIncreasedByWindows(filename):
    count = 0
    measurements = read_input(filename)

    for i in range(0, len(measurements)-2):
        cur = sum(measurements[i:i+3])
        if i != 0:
            if prev < cur:
                count += 1
        prev = cur

    return count


input_file = 'puzzle_input/day01.txt'
print(f'count increased: {countIncreased(input_file)}')
print(f'count increase by windows: {countIncreasedByWindows(input_file)}')
