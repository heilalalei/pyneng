#!/usr/bin/env python3
#Задание 9.3
def get_int_vlan_map(cfg):
    ''' Функция '''
    dict_access = {}
    dict_trunk = {}
    with open(cfg) as f:
        for line in f:
            if line.startswith('interface') and 'Ethernet' in line:
                intf = line.split()[1]
            elif 'access vlan' in line:
                vlan = line.split()[3]
                dict_access[intf] = int(vlan)
            elif 'trunk allowed' in line:
                vlan = [int(line.split()[4].split(',')[i]) for i in range(len(line.split()[4].split(',')))]
                dict_trunk[intf] = vlan
    print('Access interfaces:\n',dict_access)
    print('Trunk interfaces:\n',dict_trunk)

get_int_vlan_map('config_sw1.txt')
                    



