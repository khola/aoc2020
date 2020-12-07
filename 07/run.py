with open("input", "r") as file:
    rows = file.read().splitlines()


def split_children_colors(s):
    def strip_color(s):
        ss = s.strip()
        l = ss.split(" ")
        number = l.pop(0)
        l.pop(len(l)-1)
        return [" ".join(l), int(number)]
    l = s.split(", ")

    if (l[0] == " no other bags."):
        return False

    return list(map(strip_color, l))


bags = {}

for row in rows:
    r = row.split("contain")
    parent_color = r[0].replace(" bags ", "")
    children_colors = split_children_colors(r[1])
    if (children_colors):
        items = {}
        for k in children_colors:
            items[k[0]] = k[1]
        bags[parent_color] = items
    else:
        bags[parent_color] = False


def look_for_gold(bag):
    found = False
    if bag == False:
        return False
    if bag.get("shiny gold"):
        return True
    for key, value in bag.items():
        found = look_for_gold(bags[key]) or found
    return found


count = 0

for key, value in bags.items():
    if look_for_gold(value):
        count += 1


def count_children(bag):
    c = 1
    if bag == False:
        return c
    for name, amount in bag.items():
        c += count_children(bags[name]) * amount
    return c


print(count, count_children(bags["shiny gold"]) - 1)
