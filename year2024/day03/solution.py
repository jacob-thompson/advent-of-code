from re import finditer

MULTIPLY = "mul"
DONT = "don't"
DO = "do"

def get_corrupted_memory():
    memory = []

    with open("input.txt", "r") as file:
        for line in file:
            memory.append(line)

    return memory

def get_mul_operands(line, index):
    index += len(MULTIPLY)
    if line[index] != "(":
        return None, None
    else:
        index += 1

    dos = [m.start() for m in finditer(DO, line)]
    donts = [m.start() for m in finditer(DONT, line)]

    separated = False
    first_operand = ""
    second_operand = ""
    for char in line[index:]:
        if char.isdigit() and not separated:
            first_operand += char
        elif char == "," and first_operand != "":
            separated = True
        elif char.isdigit() and separated:
            second_operand += char
        elif char == ")" and second_operand != "":
            break
        else:
            return None, None

    return first_operand, second_operand

def get_instructions(memory):
    instructions = []
    for line in memory:
        muls = [m.start() for m in finditer(MULTIPLY, line)]

        for index in muls:
            operands = get_mul_operands(line, index)
            instructions.append(operands)

    return instructions

def get_filtered_instructions(memory):
    instructions = []
    do = True
    for line in memory:
        muls = [m.start() for m in finditer(MULTIPLY, line)]
        donts = [m.start() for m in finditer(DONT, line)]
        dos = [m.start() for m in finditer(DO, line)]

        index = 0
        for char in line:
            if index in donts: do = False
            elif index in dos: do = True
            elif index in muls and do:
                operands = get_mul_operands(line, index)
                instructions.append(operands)

            index += 1

    return instructions

def execute_instructions(instructions):
    value = 0
    for operand1, operand2 in instructions:
        if operand1 is None or operand2 is None:
            continue
        value += int(operand1) * int(operand2)

    return value

def main():
    corrupted = get_corrupted_memory()

    unfiltered_instructions = get_instructions(corrupted)
    unfiltered_sum = execute_instructions(unfiltered_instructions)
    print(unfiltered_sum)

    filtered_instructions = get_filtered_instructions(corrupted)
    filtered_sum = execute_instructions(filtered_instructions)
    print(filtered_sum)

if __name__ == "__main__":
    main()
