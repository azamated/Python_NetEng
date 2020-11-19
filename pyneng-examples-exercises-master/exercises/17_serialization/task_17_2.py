# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import re
import csv

#main function
def parse_sh_cdp_neighbors(data_string):
	#match hostname of the device
	match1 = re.search(r'^(?P<hostname>\S+)>show', data_string)
	if match1:
		device_hostname = match1.group('hostname')
	
	#separate non-valuable data
	parsed_data = data_string.split('Port ID')[1]
	matched_data  = re.findall(r'(\S+\s+\S+ \d\/\d\s+\S+\s+\S \S \S\s+\S+\s+\S+ \d\/\d)', parsed_data)
		
	#convert data to dictionary
	final_dict= {}
	temp_dict2 = {}
	for item in matched_data:
		temp_dict1 = {}
		match2 = re.search(r'(?P<deviceId>^\S+)\s+(?P<localInt>\S+ \d+/\d+)\s+\S+\s+\S \S \S\s+\S+\s+(?P<portId>\S+ \d+/\d+)', item)
		if match2:
			#Append value to temp and final dictionaries
			temp_dict1[match2.group('deviceId')] = match2.group('portId')
			temp_dict2[match2.group('localInt')] = temp_dict1
			final_dict[device_hostname] = temp_dict2
	return final_dict
	
with open('sh_cdp_n_sw1.txt') as f:
	data = f.read().replace('\n', '')
	print(parse_sh_cdp_neighbors(data))
