from ast import literal_eval
import json


first_solution = 0
second_solution = 0

with open('input') as infile:
    for line in infile:
        line = line.strip()
        first_solution += len(line) - len(literal_eval('b' + line))
        second_solution += len(json.dumps(line)) - len(line)

print(first_solution)
print(second_solution)