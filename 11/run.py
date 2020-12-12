from math import copysign, prod

with open("input", "r") as file:
    data = file.read().splitlines()


rows = list(map(list, data))


def get_el_from_direction(r, c, row, column, rows):
    step = 1
    while True:
        rr = row + step * r
        cc = column + step * c
        if rr < 0 or cc < 0:
            return "."
        try:
            curr = rows[rr][cc]

            if (curr != "."):
                return curr
            else:
                step += 1
        except IndexError:
            pass
            return "."


def get_adj_values_2(row, column, rows):

    result = [get_el_from_direction(-1, -1, row, column, rows),
              get_el_from_direction(-1, 0, row, column, rows),
              get_el_from_direction(-1, +1, row, column, rows),
              get_el_from_direction(0, -1, row, column, rows),
              get_el_from_direction(0, +1, row, column, rows),
              get_el_from_direction(+1, -1, row, column, rows),
              get_el_from_direction(+1, 0, row, column, rows),
              get_el_from_direction(+1, +1, row, column, rows)]

    return result


def check_letter(i, j, rows):
    item = rows[i][j]
    if (item == "."):
        return "."
    adj = get_adj_values_2(i, j, rows).count("#")

    if (item == "L" and adj == 0):
        return "#"
    if (item == "#" and adj >= 5):
        return "L"
    return item


def get_new_version(rows):
    new_rows = []
    for i in range(0, len(rows)):
        new_row = []
        for j in range(0, len(rows[i])):
            new_row.append(check_letter(i, j, rows))
        new_rows.append(new_row)
    return new_rows


def main():
    vers = [rows]
    vers.append(get_new_version(rows))

    while vers[len(vers)-1] != vers[len(vers) - 2]:
        vers.append(get_new_version(vers[len(vers) - 1]))

    result = 0
    for row in vers[len(vers) - 1]:
        result += row.count("#")
    return result


print(main())
