import itertools
from collections import Counter

with open('input') as infile:
    containers = sorted(int(line) for line in infile.read().strip().split('\n'))

ctr = 0
amountmap = Counter()
for combination in itertools.product((False,True), repeat=len(containers)):
    if sum(volume if enabled else 0 for volume, enabled in zip(containers, combination)) == 150:
        ctr += 1
        amountmap[sum(combination)] += 1
print(ctr)
print(amountmap[min(amountmap.keys())])
