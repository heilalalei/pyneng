#!/usr/bin/env python3
#Task 15_2a

import re
from pprint import pprint
from answer_15_2 import parse_sh_ip_int_br

def convert_to_dict(headers, tuple_of_intf):
	result = []
	for i in range(len(tuple_of_intf)):
		result.append((dict(zip(headers,list(tuple_of_intf[i])))))
		#print(list(tuple_of_intf[2]))
	return result

pprint(convert_to_dict(['interface','address','status','protocol'], parse_sh_ip_int_br('sh_ip_int_br.txt')))

