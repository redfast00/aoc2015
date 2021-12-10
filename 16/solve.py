with open('input') as infile:
    sues = {idx+1: {(spl := elempair.split(': '))[0]: int(spl[1]) for elempair in line.split(': ', maxsplit=1)[1].split(', ')} for idx, line in enumerate(infile)}

fingerprint = {(spl := line.strip().split(': '))[0]: int(spl[1]) for line in '''
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
'''.strip().split('\n')}

for sue_num, sue_attributes in sues.items():
    for attribute, value in sue_attributes.items():
        if value != fingerprint[attribute]:
            break
    else:
        print(sue_num)

for sue_num, sue_attributes in sues.items():
    for attribute, value in sue_attributes.items():
        if attribute in ('cats', 'trees'):
            if value <= fingerprint[attribute]:
                break
        elif attribute in ('pomeranians', 'goldfish'):
            if value >= fingerprint[attribute]:
                break
        elif value != fingerprint[attribute]:
            break
    else:
        print(sue_num)