from math import prod

with open("input", "r") as file:
    rows = file.read().splitlines()


def prepare_data(rows):
    data = list(map(int, rows))
    data.insert(0, 0)
    data.sort()
    data.append(data[len(data) - 1] + 3)
    return data


def combs_in_range(len):
    if len == 0 or len == 1:
        return 1
    if len == 2:
        return 2
    return combs_in_range(len-3) + combs_in_range(len-2) + combs_in_range(len-1)


def get_leaps_list(data):
    leaps = []
    current = 0
    while current < len(data):
        start = data[current]
        end = start
        while end + 1 in data:
            end += 1
        leaps.append(len(range(start, end)))
        current = data.index(end) + 1
    return leaps


data = prepare_data(rows)
leaps = get_leaps_list(data)
print(prod(list(map(combs_in_range, leaps))))
