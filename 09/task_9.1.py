#!/usr/bin/env python3
#Задание 9.1. Оно запрашивает имя файла, в который затем запишет целый конфиг на всех интерфейсы.
#Для этого используются write и join.
to_file = input('Введите имя файла, в который нужно сохранить конфиг интерфейсов access:\n')
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
def cfg_to_list(access_template_here,access_dict_here):
    '''Doc string'''
    result = []
    for intf in access_dict:
        result.append('interface {}'.format(intf))
        for line in access_template:
            if line.endswith('access vlan'):
                result.append(' '+line+' {}'.format(access_dict[intf]))
            else:
                result.append(' '+line)
    return result
#def cfg_as_file(cfg,to_file)                  
cfg_as_list = cfg_to_list(access_template,access_dict)
with open(to_file,'w') as f:
    f.write('\n'.join(cfg_as_list)+'\n')



































