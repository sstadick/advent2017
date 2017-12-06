#!/usr/bin/env python
import sys
from collections import Counter


def check_valid(line):
    counts = Counter(line.split())
    return True if not [i for i in counts.values() if i != 1] else False


def check_valid2(line):
    counts = [dict(Counter(word)) for word in line.split()]
    unique = []
    for c in counts:
        check = set([(k, v) for k, v in c.items()])
        if check not in unique:
            unique.append(check)
    return True if len(unique) == len(counts) else False


print(sum([1 for line in sys.stdin if check_valid2(line)]))
