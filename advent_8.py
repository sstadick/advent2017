#!/usr/bin/env python
import sys
from collections import defaultdict

registers = defaultdict(lambda: 0, {})
maxes = []


def convert_op(line):
    return line.replace('inc', '+=').replace('dec', '-=')


def convert_vars(line):
    values = line.split()
    for i in [0, 4]:
        values[i] = "registers[\'" + values[i] + "']"
    return ' '.join(values[3:] + [' : '] + values[:3] + ['; [maxes.append(v) for v in registers.values()]'])


[exec(convert_vars(convert_op(line)).rstrip('\n')) for line in sys.stdin.readlines()]

print(max(registers.values()))
print(max(maxes))
