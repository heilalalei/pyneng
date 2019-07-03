#!/usr/bin/env python3
#Task 15_5

import re
from pprint import pprint

def generate_description_from_cdp(cfg):
	result = {}
	with open(cfg) as f:
		for line in f:
			match = re.search('(?P<device>^\S+)\s+(?P<local_intf>\w+ \S+).+\W+(?P<port_id>\w+ \S+)',line)
			if match:
				result[match.group('local_intf')] = 'description Connected to {} port {}'.format(match.group('device'),match.group('port_id'))
				#print(match.groups())
	return result
	
pprint(generate_description_from_cdp('sh_cdp_n_sw1.txt'))
