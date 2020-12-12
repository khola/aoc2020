from math import copysign, prod

with open("input", "r") as file:
    data = file.read().splitlines()

instructions = [[x[0], int(x[1:])] for x in data]

ship = {
    "X": 0,
    "Y": 0,
}

waypoint = {
    "X": 10,
    "Y": 1,
}


def rotate(dir, value):
    steps = int(value / 90) - 1
    x = waypoint["X"]
    y = waypoint["Y"]
    rotations = []
    if dir == "R":
        rotations = [[y, -x], [-x, -y], [-y, x]]
    elif dir == "L":
        rotations = [[-y, x], [-x, -y], [y, -x]]
    X, Y = rotations[steps]
    waypoint["X"] = X
    waypoint["Y"] = Y


def move(command, value):
    if command == "F":
        ship["X"] = ship["X"] + value * waypoint["X"]
        ship["Y"] = ship["Y"] + value * waypoint["Y"]
    if command == "E":
        waypoint["X"] = waypoint["X"] + value
    if command == "W":
        waypoint["X"] = waypoint["X"] - value
    if command == "N":
        waypoint["Y"] = waypoint["Y"] + value
    if command == "S":
        waypoint["Y"] = waypoint["Y"] - value
    if command == "R":
        rotate(command, value)
    if command == "L":
        rotate(command, value)


for instruction in instructions:
    move(instruction[0], instruction[1])


print(abs(ship["X"])+abs(ship["Y"]))
