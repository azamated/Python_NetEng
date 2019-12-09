# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip = input("Please enter IP address: ")
ip_parsed = ip.split(".") 

for oct in ip_parsed:
	oct_int = int(oct)
	if oct_int in range(224):
		if oct_int == 0:
			print (ip + " is unassigned")
			break
		break
	break
		else:
			print (ip + " is unicast")
			break
		break
	break

"""
oct1 = int(ip_parsed[i])
if oct1 in range(224):
	if ip_parsed[0] == 0:
		print (ip + " is unassigned")
	else:
		print (ip + " is unicast")

"""
