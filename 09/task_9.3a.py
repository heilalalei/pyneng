#!/usr/bin/env python3
#Задание 9.3a
def get_int_vlan_map(cfg):
    ''' Функция '''
    dict_access = {}
    dict_trunk = {}
    access_check = False
    with open(cfg) as f:
        for line in f:
            if line.startswith('interface') and 'Ethernet' in line:
                intf = line.split()[1]
            elif 'mode access' in line:
                access_check = True
            elif 'access vlan' in line:
                vlan = line.split()[3]
                dict_access[intf] = int(vlan)
                access_check = False
            elif access_check == True and not 'access vlan' in line:
                dict_access[intf] = 1
                access_check = False
            elif 'trunk allowed' in line:
                vlan = [int(line.split()[4].split(',')[i]) for i in range(len(line.split()[4].split(',')))]
                dict_trunk[intf] = vlan
    print('Access interfaces:\n',dict_access)
    print('Trunk interfaces:\n',dict_trunk)

get_int_vlan_map('config_sw2.txt')
                    



