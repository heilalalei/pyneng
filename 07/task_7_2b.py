#!/usr/bin/env python3
#Задача 7.2b
ignore = ['duplex','alias','Current configuration']
with open(input('Введите имя файла конфигурации-источника:\n')) as src, open('config_sw1_cleared.txt','w') as dest:
    for line in src:
        check = True
        if line.startswith('!'):
            continue
        for word in line.split():
            for word1 in ignore:
                if word in word1:
                    check = False
        if check == False:
            continue
        else:
            dest.write(line)

