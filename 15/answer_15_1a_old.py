#!/usr/bin/env python3
#Task 15_1a_old
"""
Задание 15.1a

Напишите регулярное выражение, которое отобразит строки с интерфейсами 0/1 и 0/3 из вывода sh ip int br.
Проверьте регулярное выражение, используя скрипт, который был создан в задании 15.1, и файл sh_ip_int_br.txt.
В файле задания нужно написать только регулярное выражение.
"""
import re
import sys

#regex = sys.argv[1]
with open(sys.argv[1],'r') as f:
	for line in f:
		match = re.search('/1 |/3 ',line)
		if match:
			print(line)
		

#if __name__ == '__main__':
