#!/usr/bin/env python3
f = open(input('Введите имя файла конфигурации\n'))
for line in f:
    if line.startswith('!'):
        continue
    else:
        print(line[:len(line)-1])

