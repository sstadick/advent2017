#!/usr/bin/env python
from sys import stdin


def to_ints(vals):
    return list(map(lambda x: int(x), vals))


def sign(x):
    if x >= 0:
        return '+'
    else:
        return '-'


def hextille_distance(cord_1, cord_2):
    dx = cord_1[0] - cord_2[0]
    dy = cord_1[1] - cord_2[1]

    if sign(dx) == sign(dy):
        return abs(dx + dy)
    else:
        return max(abs(dx), abs(dy))

cord = [0, 0]
directions = {
    'n': lambda x: [x[0] - 1, x[1] + 1],
    's': lambda x: [x[0] + 1, x[1] - 1],
    'ne': lambda x: [x[0], x[1] + 1],
    'nw': lambda x: [x[0] - 1, x[1]],
    'sw': lambda x: [x[0], x[1] - 1],
    'se': lambda x: [x[0] + 1, x[1]],
    }

inputs = stdin.readline().rstrip('\n').split(',')
distances = []

for ins in inputs:
    cord = directions[ins](cord)
    distances.append(hextille_distance(to_ints(cord), [0, 0]))


print(hextille_distance(to_ints(cord), [0, 0]))
print(max(distances))
