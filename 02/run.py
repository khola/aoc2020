with open("input", "r") as file:
    passwords = file.readlines()


def check_password_1(min, max, letter, word):
    count = list(word).count(letter)
    return min <= count <= max


def check_password_2(min, max, letter, word):
    def eq(l1):
        def F(l2):
            return l1 == l2
        return F

    first = min - 1
    second = max - 1
    letters_from_word = [word[first], word[second]]
    matches = list(map(eq(letter), letters_from_word))
    return matches.count(True) == 1


positives_part_1 = 0
positives_part_2 = 0

for password in passwords:
    parts = password.split(" ")
    limits = list(map(int, parts[0].split("-")))
    letter = parts[1][0]
    word = parts[2]
    if check_password_1(limits[0], limits[1], letter, word):
        positives_part_1 += 1
    if check_password_2(limits[0], limits[1], letter, word):
        positives_part_2 += 1

print(positives_part_1)
print(positives_part_2)
