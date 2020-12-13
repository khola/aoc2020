with open("input", "r") as file:
    data = file.read().splitlines()


def part_1():
    time = int(data[0])
    buses = list(
        map(int, filter(lambda bus: (bus != "x"), data[1].split(","))))

    n = time
    result = 0
    while result == 0:
        for bus in buses:
            if (n % bus == 0):
                result = (n - time) * bus
                break
        n += 1
    print(result)


def part_2():
    busses = [[x, int(y)]
              for x, y in enumerate(data[1].split(",")) if y != "x"]
    time = 0
    step = busses[0][1]
    for bus in busses[1:]:
        while((time+bus[0]) % bus[1] != 0):
            time += step
        step *= bus[1]
    return time


print(part_2())
