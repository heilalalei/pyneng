#!/usr/bin/env python3
#Task 15_2

import re
from pprint import pprint

def parse_sh_ip_int_br(cfg):
	result = []
	with open(cfg) as f:
		for line in f:
			match = re.search('(\S+\d) +(\S+) +\S+ +\S+ +(administratively down|down|up) +(\w+)',line)
			if match:
				result.append((match.groups()))
	return result
	
if __name__ == "__main__":
	pprint(parse_sh_ip_int_br('sh_ip_int_br.txt'))
	
