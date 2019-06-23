#!/usr/bin/env python3
#Task 12.1

import ipaddress
import subprocess

def check_ip_addresses(ip_list):
	reachable_ip, unreachable_ip = [], []
	if type(ip_list) == list:
		for ip in ip_list:
			reply = subprocess.run(['ping','-c','3',ip],stdout=subprocess.DEVNULL)
			if reply.returncode == 0:
				reachable_ip.append(ip)
			else:
				unreachable_ip.append(ip)
	else:
		reply = subprocess.run(['ping','-c','3',ip_list],stdout=subprocess.DEVNULL)
		if reply.returncode == 0:
			reachable_ip.append(ip_list)
		else:
			unreachable_ip.append(ip_list)
	if __name__ == "__main__":
		print(reachable_ip, unreachable_ip)
	return reachable_ip, unreachable_ip
'''	
	print('Reachable ip addresses:') 
	print(reachable_ip,'\n')
	print('Uneachable ip addresses:')
	print(unreachable_ip)
'''	
if __name__ == "__main__":
	check_ip_addresses(['8.8.8.8','8.8.4.4','10.0.10.10'])



