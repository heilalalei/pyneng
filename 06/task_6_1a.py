#!/usr/bin/env python3
a = True
b = False
ipaddr = input("Введите IP-адрес:\n")
ip = ipaddr.split('.')
while a==True:
    if len(ip) != 4:
        print('wrong')
        a = False
        break
    for i in range(4):
        if not ip[i].isdigit():
            print('wrong2')
            a = False
            break
    if a == False:
        break
    for i in range(4):
        if not (int(ip[i]) <= 255 and int(ip[i]) >= 0):
            print('wrong3')
            a = False
            break
        else:
            b = True
            continue
    if b == False:
        break
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










'''

ipaddr = input("Введите IP-адрес:\n") 
ip = [ipaddr.split('.')
if len(ipaddr.split('.')) != 4:
    print('Incorrect address')
else:
    for i in range(len(ipaddr.split('.'))):
        if not ip[i].isdigit() and not len(ip[i]) and not (int(ip[i])<0 and int(ip[i])>255):
            print('Incorrect IPv4 address')
        else:
#            ip = [int(ipaddr.split('.')[i]) for i in range(4)]
            if ipaddr == '0.0.0.0':
                print('unassigned')
            elif ipaddr == '255.255.255.255':
                print('local broadcast')
            elif ip[0] > 0 and ip[0] <= 223:
                print('unicast')
            elif ip[0] >= 224 and ip[0] <= 239:
                print('multicast')
            else:
                print('unused')
 
'''
