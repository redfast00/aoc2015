from functools import reduce
import operator

ingredient_stats = {}
with open('input') as infile:
    for idx, line in enumerate(infile):
        ingredient, statlist = line.strip().split(': ')
        stats = {(spl := item.split())[0]: int(spl[1]) for item in statlist.split(', ')}
        ingredient_stats[idx] = stats

assert len(ingredient_stats) == 4

first_attributes = ['capacity', 'durability', 'flavor', 'texture']
max_found = 0

for i in range(100+1):
    for j in range(100+1):
        if i+j > 100:
            break
        for k in range(100+1):
            if i+j+k > 100:
                break
            l = 100 - (i + j + k)
            score = reduce(operator.mul, (max(i*ingredient_stats[0][name] + j*ingredient_stats[1][name] + k*ingredient_stats[2][name] + l*ingredient_stats[3][name],0) for name in first_attributes))
            max_found = max(score, max_found)

print(max_found)

max_found = 0

for i in range(100+1):
    for j in range(100+1):
        if i+j > 100:
            break
        for k in range(100+1):
            if i+j+k > 100:
                break
            l = 100 - (i + j + k)
            if i*ingredient_stats[0]['calories'] + j*ingredient_stats[1]['calories'] + k*ingredient_stats[2]['calories'] + l*ingredient_stats[3]['calories'] == 500:
                score = reduce(operator.mul, (max(i*ingredient_stats[0][name] + j*ingredient_stats[1][name] + k*ingredient_stats[2][name] + l*ingredient_stats[3][name],0) for name in first_attributes))
                max_found = max(score, max_found)

print(max_found)