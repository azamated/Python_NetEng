# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess


def ping_ip_addresses(ip_addresses):
	tuple_ip = ()
	ok_ip = []
	ko_ip = []
	for item in ip_addresses:
		result = subprocess.run(["ping", "-c", "3", "-n", item], stdout=subprocess.DEVNULL)
		if result.returncode == 0:
			ok_ip.append(item)
		else:
			ko_ip.append(item)
	tuple_ip = (ok_ip, ko_ip)
	return tuple_ip

print (ping_ip_addresses(['8.8.8.8', '1.1.1.1', '192.168.5.6', '4.4.4.4', '10.5.6.97']))
