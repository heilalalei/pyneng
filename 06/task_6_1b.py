#!/usr/bin/env python3
ipaddr = input('Введите X.X.X.X:\n')
while True:
    i = 0
    ii = 0
    a = True
    b = True
    ip = ipaddr.split('.')
    if len(ip) != 4: #Проверка на то, что IP состоит из 4 октетов
        ipaddr = input('Incorrect IPv4 address. Try again:\n')
        continue
    while i <= 3 and a == True: #Проверка на то, что все октеты - числа
        if not ip[i].isdigit():
            a = False
        i += 1
    if a == False:
        ipaddr = input('Incorrect IPv4 address. Try again:\n')
        continue
    while ii <= 3 and b == True: #Проверка на то, что все октеты в нужном диапазоне
        if not (int(ip[ii])>=0 and int(ip[ii])<=255):
            b = False
        ii += 1
    if b == False:
        ipaddr = input('Incorrect IPv4 address. Try again:\n')
        continue
    else:
        if ipaddr == '0.0.0.0':
            print('unassigned')
        elif ipaddr == '255.255.255.255':
            print('local broadcast')
        elif int(ip[0]) > 0 and int(ip[0]) <= 223:
            print('unicast')
        elif int(ip[0]) >= 224 and int(ip[0]) <= 239:
            print('multicast')
        else:
            print('unused')
        break





