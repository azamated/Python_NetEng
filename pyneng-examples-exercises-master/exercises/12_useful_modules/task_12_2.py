# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

'''
import subprocess

def convert_ranges_to_ip_list(ips):
	new_ip_list = []
	for item in ips:
		if '-' in item:
			iprange = item.split('-')
			range_start = iprange[0].split('.')
			if '.' not in iprange[1]:
				range_end = iprange[1]
				oct4_list = list(range(int(range_start[3]), int(range_end[0])+1))
			else:
				range_end = iprange[1].split('.')
				oct4_list = list(range(int(range_start[3]), int(range_end[3])+1))
			new_ip_string = str(range_start[0]) + '.' + str(range_start[1]) + '.' + str(range_start[2])
			for item in oct4_list:
				new_ip = new_ip_string + '.' + str(item)
				new_ip_list.append(new_ip)
		else:
			new_ip_list.append(item)
	return new_ip_list		


def ping_ip_addresses(ip_addresses):
	converted_ips = convert_ranges_to_ip_list(ip_addresses)
	tuple_ip = ()
	ok_ip = []
	ko_ip = []
	for item in converted_ips:
		result = subprocess.run(["ping", "-c", "1", "-n", item], stdout=subprocess.DEVNULL)
		if result.returncode == 0:
			ok_ip.append(item)
		else:
			ko_ip.append(item)
	tuple_ip = (ok_ip, ko_ip)
	return tuple_ip

print (ping_ip_addresses(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']))






