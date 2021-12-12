from collections import defaultdict


with open('input') as infile:
    input_number = int(infile.read().strip())

def factors(n):
    return set(x for tup in ([i, n//i]
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)


def house_1(number):
    return sum(10*f for f in factors(number))

def house_2(number):
    return sum(11*f for f in factors(number) if number / f <= 50)

ctr = 0
while (house(ctr) < input_number):
    ctr += 1
print(ctr)

ctr = 0
while (house_2(ctr) < input_number):
    ctr += 1
print(ctr)
