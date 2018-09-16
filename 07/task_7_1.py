#!/usr/bin/env python3
f = open('/home/python/pyneng/pyneng-examples-exercises/exercises/07_files/ospf.txt')
ospf_list = ['Prototol:','Prefic:','AD/Metric:','Next-Hop:','Last update:','Outbound Interface:']
for line in f:
    ospf = dict.fromkeys(ospf_list)
    i = 0
    lst = []
    for value in line.split():
        if value == 'via':
            continue
        if value == 'O':
            lst.append('OSPF')
        elif value.startswith('['):
            lst.append(value[1:len(value)-1])
        elif value.endswith(','):
            lst.append(value[:len(value)-1])
        else:
            lst.append(value)
    for key in ospf:
        ospf[key] = lst[i]
        i += 1
    for key in ospf:
        print(key,' '*(21-len(key)),ospf[key])
    print('\n')



