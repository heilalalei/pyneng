#!/usr/bin/env python3
#Задание 9.3
def get_int_vlan_map(cfg):
    ''' Функция '''
    int_list = []
    with open(cfg) as f:
        for line in f:
            if line.startswith('interface') and 'Ethernet' in line:
                int_list.append(line.split()[1])
    print(int_list)

get_int_vlan_map('config_sw1.txt')
                    



