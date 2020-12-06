with open("input", "r") as file:
    data = file.read()

groups = data.split("\n\n")
count = [0, 0]

for group in groups:
    all_answers = group.replace("\n", "")
    count[0] += len(set(all_answers))


for group in groups:
    commons = set.intersection(*map(set, group.split("\n")))
    count[1] += len(commons)

print(count)
