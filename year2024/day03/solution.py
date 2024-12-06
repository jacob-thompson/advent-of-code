from re import findall

DONT = "don't()"
DO = "do()"

with open("input.txt", "r") as file:
    data = file.read()

def compute(part1):
    result = 0
    do = True
    for instruction, op1, op2 in findall("(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", data):
        if instruction == DONT:
            do = False
        elif instruction == DO:
            do = True
        else:
            if do or part1:
                result += int(op1) * int(op2)

    return result

# part 1
print(compute(True))

# part 2
print(compute(False))
