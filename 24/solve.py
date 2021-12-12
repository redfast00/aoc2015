import itertools
import functools
import operator


with open('input') as infile:
    numbers = list(reversed(sorted(int(l.strip()) for l in infile)))

def powerset_mod(iterable):
    "powerset_mod([1,2,3]) --> () (1,) (2,) (3,)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range((len(s)//2)+1))

def subdivision_possible(numbers, selected, amount, expected_comparment_weight):
    remaining = numbers - selected
    for items in powerset_mod(remaining):
        if sum(items) == expected_comparment_weight:
            if amount == 2 or subdivision_possible(numbers, selected | set(items), amount - 1, expected_comparment_weight):
                return True
    return False

def solve(compartments):
    expected_comparment_weight = sum(numbers) // compartments
    items_in_first_compartment = 1
    found = False
    minimal_qe = float('inf')
    while not found:
        for items in itertools.combinations(numbers, items_in_first_compartment):
            s = sum(items)
            if s == expected_comparment_weight:
                if subdivision_possible(set(numbers), set(items), compartments - 1, expected_comparment_weight):
                    found = True
                    minimal_qe = min(minimal_qe, functools.reduce(operator.mul, items))
        items_in_first_compartment += 1
    return minimal_qe

print(solve(3))
print(solve(4))