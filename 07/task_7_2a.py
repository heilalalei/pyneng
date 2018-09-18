#!/usr/bin/env python3
f = open(input('Введите имя файла конфигурации:\n'))
ignore = ['duplex','alias','Current configuration']
for line in f:
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
        print(line[:len(line)-1])

