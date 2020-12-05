
with open("input", "r") as file:
    seats = file.read().splitlines()


def get_binaries_from_code(code):
    row = int(code[:7].replace("B", "1").replace(
        "F", "0"), 2)
    column = int(code[7:].replace("L", "0").replace("R", "1"), 2)
    return [row, column]


def get_ticket_id(code):
    binary_ticket = get_binaries_from_code(code)
    return binary_ticket[0] * 8 + binary_ticket[1]


results = list(map(get_ticket_id, seats))
print(max(results))


def find_missing_ids(results):
    results.sort()
    min_id = results[0]
    max_id = results[len(results) - 1]
    fullList = range(min_id, max_id)
    return list(set(fullList) - set(results))


print(find_missing_ids(results)[0])
