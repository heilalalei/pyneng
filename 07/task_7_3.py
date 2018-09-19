#!/usr/bin/env python3
#Задача 7.3
f = open('CAM_table.txt')
for line in f:
    for word in line.split():
        if '.' in word:
            print(line[:len(line)-1].replace(' DYNAMIC ',''))


