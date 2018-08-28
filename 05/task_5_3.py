#!/usr/bin/env python3
intf_mode = input('Enter interface mode (access/trunk): ')
intf_type = input('Enter interface type and number: ')
vlans = input('Enter vlan(s): ')
print(intf_mode + '\n' + intf_type + '\n' + vlans)


#a = list(intf_mode + '_template')
access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

template = access_template + trunk_template
str_template = '\n'.join(template)
a = str_template.index(intf_mode)

print('Interface ' + intf_type + '\n')
print(str_template.format(vlans))
#print(str_template)
print(a)



#print('\n'.join(access_template.format(vlans)))
