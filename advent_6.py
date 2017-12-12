#!/usr/bin/env python
import sys

buffers = [int(buff) for line in sys.stdin.readlines()
           for buff in line.split()]
index_of_max = lambda x: x.index(max(x))
seen = []
cycle_count = 0
initial_index = index_of_max(buffers)
while ','.join(map(lambda x: str(x), buffers)) not in seen:
    seen.append(','.join(map(lambda x: str(x), buffers)))
    max_i = index_of_max(buffers)
    max_value = buffers[max_i]
    buffers[max_i] = 0
    for index, one in enumerate([1]*max_value):
        curr_index = (max_i + 1 + index) % len(buffers)
        if curr_index == initial_index:
            cycle_count += 1
        buffers[curr_index] += 1

print(len(seen))
print(len(seen[seen.index(','.join(map(lambda x: str(x), buffers))):]))
