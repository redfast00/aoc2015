import re
import itertools


def parse_file(filename):
    with open(filename) as input:
        h = iter(input)
        next(h)
        items = []
        for line in h:
            m = re.match(r'.*  +(\d+) + (\d)+ + (\d)+', line)
            items.append((int(m[1]), int(m[2]), int(m[3])))
        return items

possible_armor = parse_file('armor')
possible_rings = parse_file('rings')
possible_weapons = parse_file('weapons')

possible_armor.append((0, 0, 0))
possible_rings.append((0, 0, 0))
possible_rings.append((0, 0, 0))

with open('input') as infile:
    lines = infile.readlines()
    hitpoints = int(lines[0].strip().split()[-1])
    damage = int(lines[1].strip().split()[-1])
    armor = int(lines[2].strip().split()[-1])

def combat(items):
    my_hp = 100
    my_damage = sum(item[1] for item in items)
    my_armor = sum(item[2] for item in items)
    enemy_hp = hitpoints
    enemy_damage = damage
    enemy_armor = armor
    while True:
        enemy_hp -= max(1, my_damage - enemy_armor)
        if enemy_hp <= 0:
            return True
        my_hp -= max(1, enemy_damage - my_armor)
        if my_hp <= 0:
            return False

minimal_cost = float('inf')
for weapon in possible_weapons:
    for armor_item in possible_armor:
        for ring1, ring2 in itertools.combinations(possible_rings, 2):
            items_selected = [weapon, armor_item, ring1, ring2]
            if combat(items_selected):
                total_cost = sum(i[0] for i in items_selected)
                minimal_cost = min(minimal_cost, total_cost)
print(minimal_cost)

maximal_cost = float('-inf')
for weapon in possible_weapons:
    for armor_item in possible_armor:
        for ring1, ring2 in itertools.combinations(possible_rings, 2):
            items_selected = [weapon, armor_item, ring1, ring2]
            if not combat(items_selected):
                total_cost = sum(i[0] for i in items_selected)
                maximal_cost = max(maximal_cost, total_cost)
print(maximal_cost)
