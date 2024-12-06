with open("input.txt", "r") as file:
    data = file.read().strip().splitlines()

left = [int(entry.split()[0]) for entry in data]
right = [int(entry.split()[1]) for entry in data]

# part 1
print(
    sum(
        abs(l - r) for l, r in zip(sorted(left), sorted(right))
    )
)

# part 2
print(
    sum(
        left[i] * right.count(left[i]) for i in range(len(left))
    )
)
