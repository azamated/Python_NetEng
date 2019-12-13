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


ip_range= {	
			'A':[1, 127],
			'B':[128, 191],	
			'C':[192, 223],			
			'D':[224, 239],
		  '255':[255, 255],
			'0':[0, 0],
	       }
	      
ip_packet= {	
			'A':'unicast',
			'B':'unicast',			
			'C':'unicast',			
			'D':'multicast',
		  '255':'local broadcast',
			'0':'unassigned',
		   None: "unused"
	       }
for item in ip_range:
	if int(ip_range[item][0]) <= int(ip_parsed[0]) <= int(ip_range[item][1]):
		network_class = item
		break
	else:
		network_class = None

for key, value in ip_packet.items():
	if key== network_class:
		print(value)







