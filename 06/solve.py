import re
from collections import defaultdict


actions = []

with open('input') as infile:
    for line in infile:
        line = line.strip()
        m = re.match(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', line)
        actions.append((m.group(1), (int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5)))))


m = defaultdict(lambda: False)

for action, (fromx, fromy), (tox, toy) in actions:
    if action == 'turn off':
        for x in range(fromx, tox+1):
            for y in range(fromy, toy+1):
                m[(x, y)] = False
    elif action == 'turn on':
        for x in range(fromx, tox+1):
            for y in range(fromy, toy+1):
                m[(x, y)] = True
    elif action == 'toggle':
        for x in range(fromx, tox+1):
            for y in range(fromy, toy+1):
                m[(x, y)] = not m[(x, y)]
    else:
        raise ValueError(f'Unknown action: {action}')

print(sum(m.values()))

# part 2
m = defaultdict(lambda: 0)


for action, (fromx, fromy), (tox, toy) in actions:
    if action == 'turn off':
        for x in range(fromx, tox+1):
            for y in range(fromy, toy+1):
                m[(x, y)] = max(0, m[(x, y)] - 1)
    elif action == 'turn on':
        for x in range(fromx, tox+1):
            for y in range(fromy, toy+1):
                m[(x, y)] = m[(x, y)] + 1
    elif action == 'toggle':
        for x in range(fromx, tox+1):
            for y in range(fromy, toy+1):
                m[(x, y)] = m[(x, y)] + 2
    else:
        raise ValueError(f'Unknown action: {action}')

print(sum(m.values()))