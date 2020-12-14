with open("input", "r") as file:
    data = file.read().splitlines()

clean = list(map(lambda x: x.split(" = "), data))


def get_bin(x, n): return format(x, 'b').zfill(n)


def binary_list(n):
    max = ""
    for i in range(0, n):
        max += "1"
    l = int(max, 2)
    result = []
    for i in range(0, l+1):
        result.append(list(str(format(i, 'b').zfill(n))))
    return result


def part_1(data):
    def apply_mask(mask, value):
        ms = list(str(mask))
        vs = list(str(value))
        for n in range(0, len(ms)):
            if ms[n] == "X":
                ms[n] = vs[n]
        ms = "".join(ms)
        return int(ms, 2)

    mask = ""
    memory = {}
    for key, value in data:
        if key == "mask":
            mask = value
        else:
            bin_val = get_bin(int(value), 36)
            int_val_after_mask = apply_mask(mask, bin_val)
            memory[key] = int_val_after_mask

    result = 0

    for key in memory:
        result += memory[key]

    print(result)


def part_2(data):
    def get_targets(mask, value):
        ms = list(str(mask))
        vs = list(str(value))
        for i in range(0, len(ms)):
            if ms[i] == "1":
                vs[i] = "1"

        nofX = ms.count("X")
        combinations = binary_list(nofX)

        result = []
        for combination in combinations:
            temp = vs.copy()
            combination.reverse()
            for i in range(0, len(ms)):
                if ms[i] == "X":
                    temp[i] = combination.pop()
            result.append(temp)

        return list(map(lambda x: int("".join(x), 2), result))

    mask = ""
    memory = {}
    for key, value in data:
        if key == "mask":
            mask = value
        else:
            addr = key[4:-1]
            bin_addr = get_bin(int(addr), 36)
            targets = get_targets(mask, bin_addr)
            for target in targets:
                memory[target] = int(value)
    result = 0
    for key in memory:
        result += memory[key]

    print(result)


part_2(clean)
