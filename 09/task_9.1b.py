#!/usr/bin/env python3
#Задание 9.1b. Итоговый конфиг теперь не будет записан в отдельный файл единым текстом.
#Данный скрипт возвращает не список команд, а словарь, где ключи - это интерфейсы.
#Значения словаря - это СПИСОК команд для каждого интерфейса.

port_security = [
    'switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security'
]

access_template = [                     
     'switchport mode access', 'switchport access vlan',
     'switchport nonegotiate', 'spanning-tree portfast',
     'spanning-tree bpduguard enable'
]
access_dict = {
     'FastEthernet0/12': 200,
     'FastEthernet0/14': 300,
     'FastEthernet0/16': 400,
     'FastEthernet0/17': 500
}
res = access_dict.copy()
def cfg_to_list(access_template_here,access_dict_here,psecurity = False):
    '''Doc string'''
    
    for intf in res:
        res[intf] = []
        for line in access_template:
            if line.endswith('access vlan'):
                res[intf].append(' '+line+' {}'.format(access_dict[intf]))
            else:
                res[intf].append(' '+line)
        if psecurity:                                                    
            for line in port_security:                     
                res[intf].append(' '+ line)  
    print(res)
cfg_to_list(access_template,access_dict,True)




