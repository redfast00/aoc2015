import re


with open('input') as infile:
    row, column = tuple(int(p) for p in re.findall(r'\d+', infile.read()))



def nextcode(current):
    return (current * 252533) % 33554393

def get_code(row, column):
    rowidx = 1
    colidx = 1
    current = 20151125
    while not (rowidx == row and colidx == column):
        if rowidx == 1:
            rowidx, colidx = colidx + 1, 1
        else:
            rowidx, colidx = rowidx - 1, colidx + 1
        current = nextcode(current)
    return current

print(get_code(row, column))


