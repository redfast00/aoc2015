import re
from copy import deepcopy


class AbstractGate:
    def get_value(self, lookup, a):
        if isinstance(a, int):
            return a
        else:
            return lookup[a]


class NotOp(AbstractGate):
    def __init__(self, arg1, dst):
        self.arg1 = arg1
        self.dst = dst

    def inputs(self):
        return {i for i in (self.arg1,) if isinstance(i, str)}

    def calculate(self, lookup):
        v = self.get_value(lookup, self.arg1)
        lookup[self.dst] = 0xFFFF ^ v

    def __repr__(self):
        return f'NOT {self.arg1} -> {self.dst}'


class BinOp(AbstractGate):
    LOOKUP = {
        'AND': (lambda x, y: x & y),
        'OR': (lambda x, y: x | y),
        'LSHIFT': (lambda x, y: (x << y) & 0xFFFF),
        'RSHIFT': (lambda x, y: (x >> y) & 0xFFFF)
    }
    def __init__(self, arg1, arg2, op, dst):
        self.arg1 = arg1
        self.arg2 = arg2
        self.op = op
        self.dst = dst

    def inputs(self):
        return {i for i in (self.arg1, self.arg2) if isinstance(i, str)}

    def calculate(self, lookup):
        v1 = self.get_value(lookup, self.arg1)
        v2 = self.get_value(lookup, self.arg2)
        lookup[self.dst] = self.LOOKUP[self.op](v1, v2)

    def __repr__(self):
        return f'{self.arg1} {self.op} {self.arg2} -> {self.dst}'

class ConstOp(AbstractGate):
    def __init__(self, arg1, dst):
        self.arg1 = arg1
        self.dst = dst

    def inputs(self):
        return {i for i in (self.arg1,) if isinstance(i, str)}

    def calculate(self, lookup):
        v = self.get_value(lookup, self.arg1)
        lookup[self.dst] = v

    def __repr__(self):
        return f'{self.arg1} -> {self.dst}'


def try_convert_to_number(a):
    return int(a) if a.isdigit() else a


def topsort(gates):
    res = []
    available = set()
    nextgen = []
    while gates:
        for gate in gates:
            if available.issuperset(gate.inputs()):
                res.append(gate)
                available.add(gate.dst)
            else:
                nextgen.append(gate)
        gates = nextgen
        nextgen = []
    return res


gates = []
with open('input') as infile:
    for line in infile:
        line = line.strip()
        m = re.match(r'(?:(?:(?P<notop>NOT) (?P<notarg>[a-z]+|\d+))|(?:(?P<binarg1>[a-z]+|\d+) (?P<binop>LSHIFT|AND|OR|RSHIFT) (?P<binarg2>[a-z]+|\d+))|(?P<const>[a-z]+|\d+)) -> (?P<dst>[a-z]+)', line)
        if m.group('notop') is not None:
            gates.append(NotOp(try_convert_to_number(m.group('notarg')), m.group('dst')))
        elif m.group('binop') is not None:
            gates.append(BinOp(try_convert_to_number(m.group('binarg1')), try_convert_to_number(m.group('binarg2')), m.group('binop'), m.group('dst')))
        elif m.group('const') is not None:
            gates.append(ConstOp(try_convert_to_number(m.group('const')), m.group('dst')))

sorted_gates = topsort(gates)
valuemap = {}
for gate in sorted_gates:
    gate.calculate(valuemap)
a_value = valuemap['a']
print(a_value)

# Part 2
modified_gates = [ConstOp(a_value, 'b') if g.dst == 'b' else g for g in sorted_gates]
sorted_modified_gates = topsort(modified_gates)
valuemap = {}
for gate in sorted_modified_gates:
    gate.calculate(valuemap)
print(valuemap['a'])
