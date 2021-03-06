#!/usr/bin/env python3
#Task 15_2_old
"""
Задание 15.2

Создать функцию return_match, которая ожидает два аргумента:
    имя файла, в котором находится вывод команды show
    регулярное выражение

Функция должна обрабатывать вывод команды show построчно и возвращать список подстрок, которые совпали с 
регулярным выражением (не всю строку, где было найдено совпадение, а только ту подстроку, которая совпала с выражением).
Проверить работу функции на примере вывода команды sh ip int br (файл sh_ip_int_br.txt). Вывести список всех IP-адресов 
из вывода команды. Соответственно, регулярное выражение должно описывать подстроку с IP-адресом (то есть, совпадением 
должен быть IP-адрес). Обратите внимание, что в данном случае, мы можем не проверять корректность IP-адреса, 
диапазоны адресов и так далее, так как мы обрабатываем вывод команды, а не ввод пользователя.
"""
import re
import sys

def return_match(output, regex):
	match_list = []
	with open(output,'r') as f:
		for line in f:
			match = re.search(regex,line)
			if match:
				match_list.append(match.group())
	print(match_list)
		
return_match('sh_ip_int_br.txt', '(\d+\.){3}\d+')

