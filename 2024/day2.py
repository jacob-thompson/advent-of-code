def get_reports():
    reports = []

    with open("day2.txt", "r") as file:
        for line in file:
            sequence = line.split(" ")
            numbers = [int(item) for item in sequence]
            reports.append(numbers)

    return reports

def increasing(report):
    return all(x < y and y - x <= 3 for x, y in zip(report, report[1:]))

def decreasing(report):
    return all(x > y and x - y <= 3 for x, y in zip(report, report[1:]))

def fixable(report):
    index = 0

    for number in report:
        fixed = report[:]
        fixed.pop(index)

        if increasing(fixed) or decreasing(fixed):
            return True

        index += 1

    return False

def get_counter(reports, try_fixing = False):
    counter = 0

    for report in reports:
        if increasing(report) or decreasing(report):
            counter += 1
        elif try_fixing and fixable(report):
            counter += 1

    return counter

def main():
    reports = get_reports()
    counter = get_counter(reports)
    dampened = get_counter(reports, True)
    print(counter)
    print(dampened)

if __name__ == "__main__":
    main()
