#!/usr/bin/env python3
#Task 15_1

import re
import sys

def get_ip_from_cfg(cfg):
	f = open(cfg).read()
	match = re.findall(r' ip address (\S+) +(\S+)',f)
	print(match)
				
get_ip_from_cfg('config_r1.txt')

