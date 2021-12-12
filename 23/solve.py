with open('input') as infile:
    instructions = [line.strip().split(maxsplit=1) for line in infile]

def execute(registers):
    pc = 0
    while pc in range(len(instructions)):
        opcode, arg = instructions[pc]
        if opcode == 'hlf':
            registers[arg] = registers[arg] // 2
        elif opcode == 'tpl':
            registers[arg] = registers[arg] * 3
        elif opcode == 'inc':
            registers[arg] = registers[arg] + 1
        elif opcode == 'jmp':
            pc += int(arg) - 1
        elif opcode == 'jie':
            r, offset = arg.split(', ')
            if registers[r] % 2 == 0:
                pc = pc + int(offset) - 1
        elif opcode == 'jio':
            r, offset = arg.split(', ')
            if registers[r] == 1:
                pc = pc + int(offset) - 1
        pc += 1
    return registers

print(execute({'a': 0, 'b': 0})['b'])
print(execute({'a': 1, 'b': 0})['b'])
