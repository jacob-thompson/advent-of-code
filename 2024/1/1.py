from func import get_lists, get_total_distance

def main():
    left, right = get_lists()
    total = get_total_distance(left, right)
    print(total)

if __name__ == "__main__":
    main()