with open("input", "r") as file:
    data = file.read()


def calculate(last):
    numbers = list(map(int, data.split(',')))
    counts = {}

    for index, number in enumerate(numbers):
        counts[number] = index+1

    next = 0
    for i in range(len(counts)+1, last):
        n = 0
        if next in counts:
            n = i-counts[next]
        counts[next] = i
        next = n
    print(next)


calculate(2020)
calculate(30000000)
