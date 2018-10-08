#!/usr/bin/env python3
#Задание 9.2
#Скрипт создает список команд
def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов, для которых необходимо сгенерировать конфигурацию

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''
    trunk_template = [
        'switchport trunk encapsulation dot1q', 'switchport mode trunk',
        'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
    ]

    config = []
    for intf in trunk:
        config.append('interface {}'.format(intf))
        for line in trunk_template:
            if line.endswith('allowed vlan'):
                config.append(' '+line.rstrip()+' {}'.format(','.join([str(vlan) for vlan in trunk[intf]])))
            else:
                config.append(' '+line.rstrip())
    return config
trunk_dict = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
 }

generate_trunk_config(trunk_dict)

















