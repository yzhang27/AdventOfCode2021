import collections


def read_input(filename):

    with open(filename, 'r') as f:
        line = f.readline()
        fish = line.strip().split(',')

    return fish


def simulateFish(filename, days):

    days_til_new_fish = collections.defaultdict(int)
    fish = read_input(filename)

    for f in fish:
        days_til_new_fish[int(f)] += 1

    while days > 0:
        new_days_til_new_fish = collections.defaultdict(int)
        for key, value in days_til_new_fish.items():
            if key == 0:
                new_days_til_new_fish[6] += days_til_new_fish[key]
                new_days_til_new_fish[8] = days_til_new_fish[key]
            elif key == 7:
                new_days_til_new_fish[6] += days_til_new_fish[key]
            else:
                new_days_til_new_fish[key-1] = days_til_new_fish[key]
        days_til_new_fish = new_days_til_new_fish.copy()
        days -= 1

    return sum(days_til_new_fish.values())


input_file = 'puzzle_input/day06.txt'
print(simulateFish(input_file, 80))
print(simulateFish(input_file, 256))
