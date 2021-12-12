import itertools


with open('input') as infile:
    board = [[c == '#' for c in line.strip()] for line in infile]
size = len(board)

adjacents = set(itertools.product((-1, 0, 1), repeat=2)) - set([(0, 0)])

def step(boardmap):
    new_boardmap = {}
    for (x, y), status in boardmap.items():
        neighbours_on = sum(boardmap.get((x+dx, y+dy), False) for (dx, dy) in adjacents)
        if status:
            new_boardmap[(x, y)] = neighbours_on in (2, 3)
        else:
            new_boardmap[(x, y)] = neighbours_on == 3
    return new_boardmap

boardmap = {(x, y): val for x, line in enumerate(board) for y, val in enumerate(line)}
for _ in range(100):
    boardmap = step(boardmap)

print(sum(boardmap.values()))

def step_2(boardmap):
    new_boardmap = {}
    for (x, y), status in boardmap.items():
        neighbours_on = sum(boardmap.get((x+dx, y+dy), False) for (dx, dy) in adjacents)
        if status:
            new_boardmap[(x, y)] = neighbours_on in (2, 3)
        else:
            new_boardmap[(x, y)] = neighbours_on == 3
    new_boardmap[(0, size-1)] = True
    new_boardmap[(size - 1, 0)] = True
    new_boardmap[(0, 0)] = True
    new_boardmap[(size - 1, size - 1)] = True
    return new_boardmap

boardmap = {(x, y): val for x, line in enumerate(board) for y, val in enumerate(line)}
for _ in range(100):
    boardmap = step_2(boardmap)

print(sum(boardmap.values()))