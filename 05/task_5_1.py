#!/usr/bin/env python3
ip_netw = input('Введите IP-сеть в формате X.X.X.X/XX\n ')
network = ip_netw.split('/')[0] # Определяем сеть
mask = ip_netw.split('/')[1] # Определяем маску
octet_list = network.split('.') # Список октетов сети (строчный тип данных)
octet_list = [int(octet_list[0]),int(octet_list[1]),int(octet_list[2]),int(octet_list[3])]
mask = int(mask)
# шаблон
ip_template =  '''{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
#IP
print('\nNetwork:')
print(ip_template.format(octet_list[0],(octet_list[1]),(octet_list[2]),(octet_list[3])))
#mask
bin_mask = '1' * mask + '0' * (32-mask)
print('Mask:\n/'+str(mask))
print(ip_template.format(int(bin_mask[0:8],2), int(bin_mask[8:16],2), int(bin_mask[16:24],2), int(bin_mask[24:32],2)))




