def read_input(filename):
    report = []

    with open(filename, 'r') as f:
        while line := f.readline().rstrip():
            report.append(line)

    return report


def powerConsumption(report):

    gamma, epsilon = '', ''

    for i in range(len(report[0])):
        ones = 0
        for j in range(len(report)):
            ones += int(report[j][i])
        if ones > len(report)/2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    gamma_rate = int(gamma, 2)
    epsilon_rate = int(epsilon, 2)

    return gamma_rate*epsilon_rate


def determineRating(report, most_common):

    i = 0
    while len(report) > 1 and i < len(report[0]):
        ones = 0
        for j in range(len(report)):
            ones += int(report[j][i])
        if ones >= len(report) / 2:
            if most_common == '1':
                filtered = filter(lambda num: num[i] == '1', report)
            else:
                filtered = filter(lambda num: num[i] == '0', report)
        else:
            if most_common == '1':
                filtered = filter(lambda num: num[i] == '0', report)
            else:
                filtered = filter(lambda num: num[i] == '1', report)
        report = list(filtered)
        i += 1

    return int(report[0], 2)


def lifeSupportRating(report):

    oxygen_rating = determineRating(report, '1')
    co2_rating = determineRating(report, '0')

    return oxygen_rating * co2_rating


input_file = 'puzzle_input/day03.txt'

puzzle_report = read_input(input_file)

puzzle_consumption = powerConsumption(puzzle_report)

puzzle_report = lifeSupportRating(puzzle_report)

print(f'puzzle life support rating: {puzzle_report}')