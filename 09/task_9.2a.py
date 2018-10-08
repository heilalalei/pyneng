#!/usr/bin/env python3
#Задание 9.2a
#Скрипт создает словарь, где ключ - это интерфейс, а занчение - список команд
def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/1':[10,20],
          'FastEthernet0/2':[11,30],
          'FastEthernet0/4':[17] }

    Возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

    '''
    trunk_template = [
        'switchport trunk encapsulation dot1q', 'switchport mode trunk',
        'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
    ]
    config = {}
    config = trunk_dict.copy()
    for intf in trunk:
        config[intf] = []
        for line in trunk_template:
            if line.endswith('allowed vlan'):
                config[intf].append(' '+line.rstrip()+' {}'.format(','.join([str(vlan) for vlan in trunk[intf]])))
            else:
                config[intf].append(' '+line.rstrip())
    return config
trunk_dict = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
 }

generate_trunk_config(trunk_dict)

















