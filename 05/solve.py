VOWELS = 'aeiou'
FORBIDDEN = {'ab', 'cd', 'pq', 'xy'}


def is_nice_first(s):
    return (sum(letter in VOWELS for letter in s) >= 3
            and any(first == second for first, second in zip(s, s[1:]))
            and not any((f in s) for f in FORBIDDEN))


def second_first_condition(s):
    last = None
    seen = set()
    for first_letter, second_letter in zip(s, s[1:]):
        pair = first_letter + second_letter
        if pair in seen and pair != last:
            return True
        last = None if last == pair else pair
        seen.add(pair)
    return False


def second_second_condition(s):
    for fst, thr in zip(s, s[2:]):
        if fst == thr:
            return True
    return False


def is_nice_second(s):
    # Could have also solved this with a regex, but that's boring innit
    return second_first_condition(s) and second_second_condition(s)


first_ctr = 0
second_ctr = 0
with open('input') as infile:
    for line in infile:
        line = line.strip()
        first_ctr += is_nice_first(line)
        second_ctr += is_nice_second(line)

print(first_ctr)
print(second_ctr)
