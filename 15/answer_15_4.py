#!/usr/bin/env python3
#Task 15_4

import re

def get_ints_without_description(cfg):
	intf_with_descr = []
	intf_list = []
	with open(cfg) as f:
		for line in f:
			match = re.search('^interface (?P<intf>\S+)| description (?P<descr>\S+)',line)
			#match = re.search('description',line)
			if match:
				if match.lastgroup == 'intf':
					intf = match.group(match.lastgroup)
					intf_list.append(match.group(match.lastgroup))
				elif match.lastgroup == 'descr':
					intf_with_descr.append(intf)
					
	return list(set(intf_list) - set(intf_with_descr))
		
print(get_ints_without_description('config_r1.txt'))


