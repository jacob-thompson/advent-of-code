def get_lists():
    left = list()
    right = list()

    with open("input.txt", "r") as file:
        for line in file:
            numbers = line.split("   ")
            left.append(numbers[0])
            right.append(numbers[1][:-1]) # must trim newlines from right

    left.sort()
    right.sort()

    return left, right

def get_total_distance(left_list, right_list):
    total = 0

    for left, right in dict(zip(left_list, right_list)).items():
        total += abs(int(left) - int(right))

    return total

def get_similarity_score(left_list, right_list):
    similarity = 0

    for left_value in left_list:
        appearances = 0
        for right_value in right_list:
            if left_value == right_value:
                appearances += 1
        similarity += int(left_value) * appearances

    return similarity

def main():
    left, right = get_lists()
    total = get_total_distance(left, right)
    similarity = get_similarity_score(left, right)
    print(total)
    print(similarity)

if __name__ == "__main__":
    main()
