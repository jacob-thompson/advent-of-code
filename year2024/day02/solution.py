from itertools import pairwise

def safe_check(report):
    return all(
        1 <= abs(a - b) <= 3
        for a, b in pairwise(report)) and (
            report == sorted(report) or report == sorted(report)[::-1])

def dampened_safe_check(report):
    return any(
        safe_check(report[:i] + report[i + 1:])
        for i in range(len(report))
    )

with open("input.txt", "r") as file:
    data = file.read().strip().splitlines()

reports = [list(map(int, entry.split())) for entry in data]

# part 1
print(sum(safe_check(report) for report in reports))

# part 2
print(sum(dampened_safe_check(report) for report in reports))
