with open("input", "r") as file:
    fileContents = file.read()

numbers = list(map(int, fileContents.splitlines()))
for n in numbers:
    for m in numbers:
        rest = 2020 - n - m
        if rest in numbers:
            print(rest * n * m)
            break
    else:
        continue
    break
