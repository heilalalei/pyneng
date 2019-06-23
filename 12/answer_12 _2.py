#!/usr/bin/env python3
#Task 12.2

import ipaddress
import subprocess
from answer_12_1 import check_ip_addresses

def determine_min_max_ip(ip_list):
	ip_min = ''
	ip_max = ''
	if ip_list.count('.') <= 3:
		ip_min = ip_list[:ip_list.find('-')]
		ip_max = '.'.join(ip_list.split('.')[:3]) + '.' + ip_list[ip_list.find('-')+1:]
		prefixlen = determine_prefixlen(ip_min,ip_max)
	elif ip_list.count('.') > 3:
		ip_min = ip_list[:ip_list.find('-')] 
		ip_max = ip_list[ip_list.find('-')+1:]
		prefixlen = determine_prefixlen(ip_min,ip_max)
	return ip_min, ip_max, prefixlen
	
		
def determine_prefixlen(ip_min, ip_max):
	bit_min = '{:08b}'.format(int(ip_min.split('.')[-1]))
	bit_max = '{:08b}'.format(int(ip_max.split('.')[-1]))
	i = 0
	prefixlen = 24
	while bit_min[i] == bit_max[i]:
		i += 1
	return prefixlen + i	
	
def check_ip_availability():	
	ip_netw = ''
	ip_list = input('Input ip address or range of ip addresses using format x.x.x.x-x:\n')
	if '-' in ip_list:
		ip_min, ip_max, prefixlen = determine_min_max_ip(ip_list)
		ip_netw = '.'.join(ip_min.split('.')[:3]) + '.' + str(int((str('{:08b}'.format(int(ip_min.split('.')[-1])))[:prefixlen-24] + '0'*(32-prefixlen)),2))
		subnet = ipaddress.ip_network(ip_netw + '/' + str(prefixlen))
		ip_list1 = []
		for ip in subnet:
			if ip > ipaddress.ip_address(ip_max):
				break
			ip_list1.append(str(ip))
		check_ip_addresses(ip_list1)
	else:
		check_ip_addresses(ip_list)
	
if __name__ == "__main__":
	check_ip_availability()
