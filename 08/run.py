with open("input", "r") as file:
    tape = file.read().splitlines()

acc = 0


def get_instruction_details(input):
    return [input[0:3], input[4:]]


def compute(step, tape):
    global acc

    if step > len(tape):
        return "panic"
    if step == len(tape):
        return "success"

    instruction, value = get_instruction_details(tape[step])

    if (instruction == "jmp"):
        return step + int(value)
    elif (instruction == "acc"):
        acc += int(value)
    elif (instruction == "hal"):
        return "halt"

    return step+1


def check_tape(tape):
    nextStep = 0
    while nextStep != "halt":
        step = nextStep
        nextStep = compute(nextStep, tape)
        if (nextStep == "panic"):
            return False
        if (nextStep == "success"):
            return True
        tape[step] = "hal 000"
    return False


for n in range(0, len(tape) - 1):
    acc = 0
    instruction, value = get_instruction_details(tape[n])

    if instruction == "jmp" or instruction == "nop":
        patchedTape = tape.copy()
        if instruction == "jmp":
            patchedTape[n] = "nop" + value
        else:
            patchedTape[n] = "jmp" + value
        if check_tape(patchedTape):
            break
    else:
        continue

print(acc)
