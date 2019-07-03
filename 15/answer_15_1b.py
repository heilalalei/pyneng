#!/usr/bin/env python3
#Task 15_1b
"""
ДОРЕШИТЬ. проблема в том, что я не могу добавить кортежик с ипом и маской в список, если в этом списке уже есть они. 
Не могу сделать проверку на наличие/отсутствие чего либо в Value словаря result для данного интерфейса. Ругается на 
то, что еще не объявили, либо на то, что нет ключа ''.
"""
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
					result[intf] = []
				elif match.lastgroup == 'mask':
					ipaddr = match.group('ipaddr')	
					mask = match.group('mask')
					#result[intf] = [((ipaddr, mask))]
					#result[intf].append((ipaddr, mask))
					#else:
				#		result[intf] = [((ipaddr, mask))]
					
	return result			
			
pprint(get_ip_from_cfg('config_r1.txt'))
