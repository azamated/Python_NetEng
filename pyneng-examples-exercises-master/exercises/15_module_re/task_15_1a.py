# -*- coding: utf-8 -*-
'''
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''



import re
from pprint import pprint

def get_ip_from_cfg(input_data):
	result = {}

	with open(input_data) as f:
		for line in f:
			if line.startswith('interface'):
				match1 =  re.search('interface (?P<intf>\S+)', line)				 
				if  match1:
					interface = match1.group('intf')
					#print (interface)
			elif line.startswith(' ip address'):
				match2 = re.search(' ip address (?P<ipaddr>\d+\.\d+\.\d+\.\d+)\s(?P<mask>\d+\.\d+\.\d+\.\d+)',line)
				if match2:
					ip = match2.group('ipaddr')
					mask = match2.group('mask')
					result[interface] = ip, mask
					
	return result 
				
				
	
pprint (get_ip_from_cfg('config_r1.txt'))



