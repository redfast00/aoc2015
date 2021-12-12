import re
import itertools
import random


with open('input') as infile:
    lines = infile.readlines()
    compound = lines[-1].strip()
    rules = [tuple(l.strip().split(' => ')) for l in lines[:-2]]

def replace_nth(original, sub, replacement, n):
    where = [m.start() for m in re.finditer(sub, original)][n]
    before = original[:where]
    after = original[where:]
    return before + after.replace(sub, replacement, 1)



def replace_one(compound, rules):
    compounds = set()
    for rule in rules:
        amount = len(re.findall(rule[0], compound))
        for idx in range(amount):
            compounds.add(replace_nth(compound, rule[0], rule[1], idx))
    return compounds

print(len(replace_one(compound, rules)))

# There's only one unique way to invert the compound
# this is a bad solution, but it works (takes about 2 restarts)
def invert(compound, rules):
    count = 0
    while compound != 'e':
        sorted_rules = sorted(rules, key=(lambda x: random.random()))
        for rule in sorted_rules:
            if rule[1] in compound:
                amount = len(re.findall(rule[1], compound))
                idx = random.randint(0, amount - 1)
                compound = replace_nth(compound, rule[1], rule[0], idx)
                count += 1
                break
        else:
            return None
    return count

while (res := invert(compound, rules)) is None:
    pass
print(res)
