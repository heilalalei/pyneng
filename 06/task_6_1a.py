#!/usr/bin/env python3

ipaddr = input("Введите IP-адрес:\n") 
ip = [ipaddr.split('.')[i] for i in range(4)]
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
 

