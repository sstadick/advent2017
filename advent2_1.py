#!/usr/bin/env python

input_file = './inputs/advent2_1.txt'

def clean_divisor(values):
    the_one = [(v, i) for v in values for i in values if v != i and v % i == 0]
    print(values)
    print(the_one)
    return the_one[0][0] / the_one[0][1]

diffs = []
with open(input_file, 'r') as in_fh:
    for line in in_fh:
        values = list(map(int, line.split()))
        #diffs.append((max(values) - min(values)))  # Advent 2.2 calculator
        diffs.append(clean_divisor(values))  # Advent 2.2 calculator

print(sum(diffs))
