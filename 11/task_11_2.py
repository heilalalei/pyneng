#!/usr/bin/env python3
#Task 11.2

from task_11_1 import parse_cdp_neighbors
from draw_network_graph import draw_topology

draw_topology(parse_cdp_neighbors('sw1_sh_cdp_neighbors.txt'))
