with open("input", "r") as file:
    rows = file.read().splitlines()

tape = list(map(int, rows))


def find_components(sum, list):
    for n1 in list:
        for n2 in list:
            if (n2 != n1 and n1 + n2 == sum):
                return True
    return False


def part_1():
    for i in range(24, len(tape) - 1):
        start = i
        end = i+25
        has_components = find_components(tape[i + 25], tape[start:end])
        if has_components is False:
            return tape[i + 25]


result_1 = part_1()
print(result_1)


def sum_list(list):
    sum = 0
    for n in list:
        sum += n
    return sum


def find_components(sum, tape):
    for i in range(0, len(tape) - 1):
        for j in range(i, len(tape) - 1):
            test = sum_list(tape[i:j])
            if test == sum:
                r = tape[i:j]
                r.sort()
                return r[0] + r[-1]
            elif test > sum:
                break


print(find_components(result_1, tape))
