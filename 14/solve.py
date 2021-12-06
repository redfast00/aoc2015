import re
from collections import Counter

with open('input') as infile:
    stats = [tuple(int(p) for p in re.findall(r'\d+', line)) for line in infile]

def reindeer_distance(stat, time):
    speed, duration, rest_time = stat
    distance = 0
    sprint_rests = time // (duration + rest_time)
    distance += sprint_rests * speed * duration
    time -= sprint_rests * (duration + rest_time)
    remaining_sprint_time = min(duration, time)
    distance += speed * remaining_sprint_time
    return distance

print(max(reindeer_distance(stat, 2503) for stat in stats))

def live_reindeer_distance(stat):
    speed, duration, rest_time = stat
    distance = 0
    while True:
        for _ in range(duration):
            distance += speed
            yield distance
        for _ in range(rest_time):
            yield distance

timer = 0
scores = [0 for _ in stats]
for distances in zip(*list(live_reindeer_distance(s) for s in stats)):
    current_lead_distance = max(distances)
    for idx, distance in enumerate(distances):
        if distance == current_lead_distance:
            scores[idx] += 1
    timer += 1
    if timer == 2503:
        break
print(max(scores))
