# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
'''

import re

int_with_desc = []

def get_ints_without_description(input_data):
	with open (input_data) as f:
		for line in f.read().split('\n'):
			match1 = re.search('^interface (\S+$)', line)
			match2 = re.search('^ description', line)
			if match1:
				int_with_desc.append(match1.group(1))
			elif match2:
				int_with_desc.pop()
		return (int_with_desc)
		
print (get_ints_without_description('config_r1.txt'))



