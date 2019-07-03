#!/usr/bin/env python3
#Task 15_1a

import re
from pprint import pprint
def get_ip_from_cfg(cfg):
	regex = ('interface (?P<intf>\S+)| ip address (?P<ipaddr>\S+) (?P<mask>\S+)')
	result = {}
	
	with open(cfg) as f:
		for line in f:
			match = re.search(regex,line)
			if match:
				if match.lastgroup == 'intf':
					intf = match.group(match.lastgroup)
					
				elif match.lastgroup == 'mask':
					ipaddr = match.group('ipaddr')	
					mask = match.group('mask')	
					result[intf] = (ipaddr, mask)
	return result			
			
pprint(get_ip_from_cfg('config_r1.txt'))
