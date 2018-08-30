#!/usr/bin/env python3
from sys import argv
host,mask = argv[1:]

octet_list = host.split('.') # Список октетов сети (строчный тип данных)
octet_list = [int(octet_list[0]),int(octet_list[1]),int(octet_list[2]),int(octet_list[3])]
mask = int(mask)
# шаблон
ip_template =  '''{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
bit_template = '''{0:08b}{1:08b}{2:08b}{3:08b}'''
bit_sequence = bit_template.format(octet_list[0],(octet_list[1]),(octet_list[2]),(octet_list[3])) #Строчны тип
network = bit_sequence[0:mask] + '0'*(32-mask)

print('\n\nHost:')
print(ip_template.format(int(bit_sequence[0:8],2), int(bit_sequence[8:16],2), int(bit_sequence[16:24],2), int(bit_sequence[24:32],2)))
print('-'*40 + '\n')

print('Network:')
print(ip_template.format(int(network[0:8],2), int(network[8:16],2), int(network[16:24],2), int(network[24:32],2)))
print('-'*40 + '\n')

bin_mask = '1' * mask + '0' * (32-mask)
print('Mask:\n/'+str(mask))
print(ip_template.format(int(bin_mask[0:8],2), int(bin_mask[8:16],2), int(bin_mask[16:24],2), int(bin_mask[24:32],2)))

