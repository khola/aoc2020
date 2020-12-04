with open("input", "r") as file:
    data = file.read()


def is_true(val):
    return val


def split_height_string(val):
    if (len(val)) < 4:
        return [0, "cm"]
    number = ""
    for i in range(len(val) - 2):
        number = number + val[i]
    return [int(number), val[-2:]]


def is_hex_color(s):
    ss = s[1:7]
    if s[0] == "#":
        return bool(int(ss, 16))
    else:
        return False


def is_eye_color(s):
    return ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].count(s) > 0


def validators(key_val_pair):
    field = key_val_pair[0]
    value = key_val_pair[1]
    if field == "byr":
        return 1920 <= int(value) <= 2002
    if field == "iyr":
        return 2010 <= int(value) <= 2020
    if field == "eyr":
        return 2020 <= int(value) <= 2030
    if field == "hgt":
        height = split_height_string(value)
        if height[1] == "cm":
            return 150 <= height[0] <= 193
        if height[1] == "in":
            return 59 <= height[0] <= 76
    if field == "hcl":
        return is_hex_color(value)
    if field == "ecl":
        return is_eye_color(value)
    if field == "pid":
        return len(value) == 9 and bool(int(value))
    return False


def is_valid_passport(passport_key_values):
    def no_cid(key_value):
        return key_value[0] != "cid"
    passport_key_values_no_cid = list(filter(no_cid, passport_key_values))
    validations = list(map(validators, passport_key_values_no_cid))
    if len(passport_key_values_no_cid) == 7:
        return validations.count(False) == 0
    return False


def get_passport_keys_validation(passport):
    def get_key_value(key_value):
        return [key_value[0:3], key_value[4:]]
    return is_valid_passport(list(map(get_key_value, passport.replace("\n", " ").split(" "))))


validated_passports = list(
    map(get_passport_keys_validation, data.split("\n\n")))

print(validated_passports.count(True))
