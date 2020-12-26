from collections import Counter

DIRECTION_MAPPING = {
    '^': (0, 1),
    'v': (0, -1),
    '<': (-1, 0),
    '>': (1, 0)
}

with open('input') as infile:
    directions = infile.read()


def solve_first(directions):
    visited = Counter()
    cx, cy = (0, 0)
    visited[(cx, cy)] += 1
    for direction in directions:
        dx, dy = DIRECTION_MAPPING[direction]
        cx, cy = cx + dx, cy + dy
        visited[(cx, cy)] += 1
    return len(visited)


def solve_second(directions):
    visited = Counter()
    sx, sy = (0, 0)
    rx, ry = (0, 0)
    visited[(sx, sy)] += 1
    visited[(rx, ry)] += 1
    for direction_santa, direction_robo in zip(directions[::2], directions[1::2]):
        dsx, dsy = DIRECTION_MAPPING[direction_santa]
        sx, sy = sx + dsx, sy + dsy
        visited[(sx, sy)] += 1
        drx, dry = DIRECTION_MAPPING[direction_robo]
        rx, ry = rx + drx, ry + dry
        visited[(rx, ry)] += 1
    return len(visited)

print(solve_first(directions))
print(solve_second(directions))
