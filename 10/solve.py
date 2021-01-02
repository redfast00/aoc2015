with open('input') as infile:
    i = infile.read().strip()


def next_generation(s):
    '''Transforms into next string (works with both lists and strings)
    >>> next_generation('1')
    '11'
    >>> next_generation('11')
    '21'
    '''
    current_char = s[0]
    amount = 1
    output = []
    for char in s[1:]:
        if char == current_char:
            amount += 1
        else:
            output.extend(str(amount) + current_char)
            current_char = char
            amount = 1
    output.extend(str(amount) + current_char)
    return output


current = i
for _ in range(40):
    current = next_generation(current)
print(len(current))
for _ in range(10):
    current = next_generation(current)
print(len(current))
