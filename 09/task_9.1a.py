#!/usr/bin/env python3
#Задание 9.1a. Оно запрашивает имя файла, в который затем запишет целый конфиг на всех интерфейсы.
#Для этого используются write и join.

#В отличие от 9.1, появилась возможность добавить конфиг port_security. 
#По умолчанию, параметр psecurity = False, но функция в скрипте вызывается с аргументом True.
to_file = input('Введите имя файла, в который нужно сохранить конфиг интерфейсов access:\n')
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
def cfg_to_list(access_template_here,access_dict_here,psecurity = False):
    '''Doc string'''
    result = []
    for intf in access_dict:
        result.append('interface {}'.format(intf))
        for line in access_template:
            if line.endswith('access vlan'):
                result.append(' '+line+' {}'.format(access_dict[intf]))
            else:
                result.append(' '+line)
        if psecurity:                                                    
            for line in port_security:                     
                result.append(' '+ line)  
    return result
#def cfg_as_file(cfg,to_file)                  
cfg_as_list = cfg_to_list(access_template,access_dict,True)
with open(to_file,'w') as f:
    f.write('\n'.join(cfg_as_list)+'\n')







