import re
from collections import defaultdict
import itertools

happiness = {}


def score_for_arrangement(seating_arrangement, combined_happiness):
    total = 0
    first = seating_arrangement[-1]
    for second in seating_arrangement:
        total += combined_happiness[frozenset((first, second))]
        first = second
    return total


def find_best_seating(all_names, combined_happiness):
    selected_arrangement = None
    best_score = -float('inf')
    for seating_arrangement in itertools.permutations(all_names):
        score = score_for_arrangement(seating_arrangement, combined_happiness)
        if score > best_score:
            best_score = score
            selected_arrangement = seating_arrangement
    return best_score, selected_arrangement

with open('input') as infile:
    for line in infile:
        line = line.strip()
        m = re.match(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).', line)
        firstname = m.group(1)
        multiplier = -1 if m.group(2) == 'lose' else 1
        amount = int(m.group(3))
        secondname = m.group(4)
        happiness[(firstname, secondname)] = multiplier * amount

combined_happiness = defaultdict(lambda: 0)
all_names = set()
for names, value in happiness.items():
    combined_happiness[frozenset(names)] += value
    all_names.update(names)


best_score, _ = find_best_seating(all_names, combined_happiness)
print(best_score)

best_score, _ = find_best_seating(all_names | {'Me'}, combined_happiness)
print(best_score)
