import networkx

def get_rules_and_updates():
    with open("input.txt") as file:
        data = file.read().strip().split("\n\n")

    rules = [tuple(map(int, l.split("|"))) for l in data[0].split("\n")]
    updates = [tuple(map(int, l.split(","))) for l in data[1].split("\n")]

    return rules, updates

def main():
    rules, updates = get_rules_and_updates()

    unsorted_updates = {
        update for update in updates
        if any(
            a in update and b in update and update.index(a) > update.index(b)
            for a, b in rules
        )
    }
    print(
        sum(
            update[len(update) // 2] for update in updates if update not in unsorted_updates
        )
    )

    sorted_updates = [
        list(
            networkx.topological_sort(
                networkx.DiGraph((a, b) for a, b in rules if a in update and b in update)
            )
        )
        for update in unsorted_updates
    ]
    print(sum(update[len(update) // 2] for update in sorted_updates))

if __name__ == "__main__":
    main()
