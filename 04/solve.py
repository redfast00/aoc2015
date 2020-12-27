from hashlib import md5

with open('input') as infile:
    challenge = infile.read()


def first(challenge):
    c = challenge.encode('utf8')
    current = -1
    while True:
        current += 1
        if md5(c + str(current).encode('utf8')).hexdigest().startswith('00000'):
            return current

def second(challenge):
    c = challenge.encode('utf8')
    current = -1
    while True:
        current += 1
        if md5(c + str(current).encode('utf8')).hexdigest().startswith('000000'):
            return current

print(first(challenge))
print(second(challenge))