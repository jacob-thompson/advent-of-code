from itertools import count

UP = "^"
DOWN = "v"
RIGHT = ">"
LEFT = "<"
DIRECTIONS = {UP, DOWN, LEFT, RIGHT}

OBSTRUCTION = "#"
PATH = "."

LOOP_LIMIT = 10000

class Guard:
    def __init__(self, direction, x, y):
        self.direction: str = direction
        self.x: int = x
        self.y: int = y
        self.visited: set = {(self.x, self.y)}

    def change_pos(self):
        if self.direction == UP:
            if data[self.y - 1][self.x] == OBSTRUCTION:
                self.direction = RIGHT
            else:
                self.y -= 1
                self.visited.add((self.x, self.y))
        elif self.direction == DOWN:
            if data[self.y + 1][self.x] == OBSTRUCTION:
                self.direction = LEFT
            else:
                self.y += 1
                self.visited.add((self.x, self.y))
        elif self.direction == RIGHT:
            if data[self.y][self.x + 1] == OBSTRUCTION:
                self.direction = DOWN
            else:
                self.x += 1
                self.visited.add((self.x, self.y))
        elif self.direction == LEFT:
            if data[self.y][self.x - 1] == OBSTRUCTION:
                self.direction = UP
            else:
                self.x -= 1
                self.visited.add((self.x, self.y))

    def simulate(self):
        for steps in count():
            if steps == LOOP_LIMIT:
                return steps

            try:
                self.change_pos()
            except IndexError:
                return steps


with open("input.txt") as file:
    data = file.read().strip().splitlines()

# get start point
guard = None
for y_index, line in enumerate(data):
    for x_index, node in enumerate(line):
        if node in DIRECTIONS:
            guard = Guard(node, x_index, y_index)

assert guard is not None

# part 1
guard.simulate()
unique_nodes = guard.visited
print(len(unique_nodes))
