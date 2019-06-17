#!/usr/bin/env python3
#Task 11.1

def parse_cdp_neighbors(output):
	result = {}
	local_intf = []
	remote_intf = []
	remote_device = []
	local_device_list = []
	local_device = ''
	dkeys = []
	dvalues = []
	counter = 0
	with open(output) as f:
		line_checker = False
		for line in f:
			if '>' in line:
				local_device = line[0:line.find('>')]
			if line.startswith('Device ID'):
				line_checker = True
				continue
			if line_checker and not line == '\n':
				counter += 1
				remote_device.append(line.split('  ')[0])
				remote_intf.append(''.join((line.split()[-2:])))
				local_intf.append(''.join((line.split()[1:3])))
				local_device_list.append(local_device)
	dkeys = zip(local_device_list,local_intf)
	dvalues = zip(remote_device,remote_intf)
	result = dict(zip(dkeys,dvalues))
	if __name__ == '__main__':
		print(result)
	return result

		
parse_cdp_neighbors('sw1_sh_cdp_neighbors.txt')
