#!/usr/bin/env python3
#Задача 7.3a
f = open('CAM_table.txt')
vlans = []
for line in f:
    vlans.append(line.split()[0])
    for word in line.split():
        if '.' in word:
            print(line[:len(line)-1].replace(' DYNAMIC ',''))
print(vlans)

