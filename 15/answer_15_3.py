#!/usr/bin/env python3
#Task 15_3

import re
def convert_ios_nat_to_asa(ios,asa):
	asa_template = '''object network LOCAL_{}\n host {}\n nat (inside,outside) static interface service tcp {} {}\n'''	
	regex = '(?P<ip>\d+\.\d+\.\d+\.\d+)\s+(?P<global_port>\d+)\s+\S+\s+\S+\s+(?P<local_port>\d+)'
	
	with open(ios) as ios, open(asa,'w') as asa:
		for line in ios:
			match = re.search(regex, line)
			if match:
				asa.write(asa_template.format(match.group(1),match.group(1),match.group(2),match.group(3)))
convert_ios_nat_to_asa('cisco_nat_config.txt','asa_kek.txt')
