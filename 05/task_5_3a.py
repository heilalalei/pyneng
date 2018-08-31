#!/usr/bin/env python3
kek = {
'access':'Enter VLAN number: ',
'trunk':'Enter allowed VLANs: '
} 

interface_mode = input('Enter interface mode (access/trunk): ')
interface = input('Enter interface type and number: ')
vlans = input(kek[interface_mode])
print(interface_mode + '\n' + interface + '\n' + vlans)

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

kek = template[5]
template.remove(kek)
template.insert(6,kek)

b = template.index('switchport mode ' + interface_mode)
print('\nInterface ' + interface)
lol = template[5]
template.remove(lol)
template.insert(6,lol)
print(('\n'.join(template[b:5 + b])).format(vlans))


