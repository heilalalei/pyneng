#!/usr/bin/env python3

ipaddr = input("Введите IP-адрес:\n")
ip_str_list = ipaddr.split('.')
ip = [int(ip_str_list[i]) for i in range(4)]
'''
a = True
while a == True:
    ipaddr = input("Введите IP-адрес:\n")
    ip_str_list = ipaddr.split('.')
    ip = [int(ip_str_list[i]) for i in range(4)] 
    for i in range(4):
        if ip[i] >= 0 and ip[i] <= 255:
            continue
        else:
            print('Неверный формат ипчика. Введите его снова:\n')    
            a = False
            break
    continue
''' 
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

