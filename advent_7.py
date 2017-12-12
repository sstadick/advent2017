#!/usr/bin/env python
import sys
import re


tower_weights = {}
def sum_tower(node, node_map):
    if node['connections'][0] == '':
        tower_weights[node['name']] = node['weight']
        return node['weight']

    tower_weight = sum([node['weight']] + [sum_tower(node_map[c], node_map) for c in node['connections']])
    tower_weights[node['name']] = tower_weight
    return tower_weight


nodes = []
for line in sys.stdin.readlines():
    try:
        name, raw_weight, _, connections_raw = line.split(maxsplit=3)
    except ValueError as e:
        name, raw_weight = line.split()
        connections_raw = ''
    nodes.append({'name': name,
                  'weight': int(re.sub(r'\(|\)', '', raw_weight)),
                  'connections': list(map(lambda x: x.strip(), connections_raw.rstrip('\n').split(',')))})

nodes_connected_to = set([c for node in nodes for c in node['connections']])
node_names = set([n['name'] for n in nodes])
root = node_names - nodes_connected_to
node_map = {node['name']:node for node in nodes}
# print(sum_tower(node_map[list(root)[0]], node_map))
print([(c, sum_tower(node_map[c], node_map)) for c in node_map[list(root)[0]]['connections']])
for tower in tower_weights.keys():
    if len(set([tower_weights[c] for c in node_map[tower]['connections'] if c != ''])) != 1 and node_map[tower]['connections'] != ['']:
        print(tower, tower_weights[tower], node_map[tower], [(tower_weights[c], node_map[c]) for c in node_map[tower]['connections']])

# Hurray for manually looking at that final output! barf
# print(root)  # 7.1


