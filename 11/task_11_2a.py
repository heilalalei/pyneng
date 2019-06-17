#!/usr/bin/env python3
#Task 11.2a

from task_11_1 import parse_cdp_neighbors
from draw_network_graph import draw_topology

#Stick cdp output of every device together
result = {}
common_dict = {}
common_dict = parse_cdp_neighbors('sh_cdp_n_sw1.txt')
common_dict.update(parse_cdp_neighbors('sh_cdp_n_r1.txt'))
common_dict.update(parse_cdp_neighbors('sh_cdp_n_r2.txt'))
common_dict.update(parse_cdp_neighbors('sh_cdp_n_r3.txt'))

#Get rid of coincidence
keys_list = list(common_dict.keys())
values_list = list(common_dict.values())

for position,key in enumerate(keys_list):
	if key in values_list:
		keys_list.pop(position)
		values_list.pop(position)

result = dict(zip(keys_list,values_list))

draw_topology(result)
