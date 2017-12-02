#!/usr/bin/env python

input_file = '/Users/pgdx-seth/git/advent2017/inputs/advent2_1.txt'

diffs = []
with open(input_file, 'r') as in_fh:
    for line in in_fh:
        values = list(map(int, line.split()))
        print(values)
        diffs.append((max(values) - min(values)))

print(sum(diffs))
