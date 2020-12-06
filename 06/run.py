with open("input", "r") as file:
    data = file.read()

groups = data.split("\n\n")
count = [0, 0]

for group in groups:
    all_answers = group.replace("\n", "")
    count[0] += len(set(all_answers))


for group in groups:
    all_answers = list(map(list, group.split("\n")))
    commons = set.intersection(map(set, all_answers))
    count[1] += len(commons)

print(count)
