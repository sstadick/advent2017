#!/usr/bin/env python
import sys
import re
from collections import Counter

diffs = []

def remove_cancels(line):
    while '!' in line:
        line = re.sub(r'!.{1}', '', line)
    return line

def remove_garbage(line):
    while '<' in line and '>' in line:
        g_left = line.find('<')
        g_right = line.find('>')
        diffs.append(g_right - 1 - g_left)
        line = line[:g_left] + line[g_right+1:]
    return line

def count_groups(line):
    total = 0
    depth = 0
    for c in line:
        if c == '{':
            depth += 1
        elif c == '}':
            total += depth
            depth -= 1
        elif c == ',':
            continue
    return total

print(count_groups(remove_garbage(remove_cancels(sys.stdin.readlines()[0].rstrip('\n')))))
print(sum(diffs))
