# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def parse_cdp_neighbors(command_output):
	output = command_output.split('\n')
	final_dict = {}
	for line in output:
		if line.startswith('SW'):
			line_parse = line.split('>')
			deviceid = (line_parse[0])        #device as first element of tuple
		elif line.startswith('R'):
			temp_list_keys = []
			temp_list_keys.append(deviceid)
			temp_list_values = []
			
			line_parse = line.split()
			intf = line_parse[1] + line_parse[2]    	  #local interfaces for the device
			neighbour = line_parse[0] 					  #neighbours for the device
			portid = line_parse[-2] + line_parse[-1]      #neighbours' ports
			
			temp_list_keys.append(intf)               
			keys = tuple(temp_list_keys) 				  #dict key - tuple
			temp_list_values.append(neighbour) 				
			temp_list_values.append(portid)               
			values = tuple(temp_list_values)  			   #dict value - tuple
			
			final_dict[keys] = values
	return final_dict


with open('sh_cdp_n_sw1.txt') as file:
	show = file.read()
print (parse_cdp_neighbors(show))



"""def parse_cdp_neighbors(command_output):
	final_dict = {}
	with open(command_output) as f:
		for line in f:
			if line.startswith('SW'):
				line_parse = line.strip().split('>')
				device = (line_parse[0])   					 #device as first element of tuple
			elif line.startswith('R'):
				temp_list_keys = []
				temp_list_keys.append(device)
				temp_list_values = []
				
				line_parse = line.strip().split()
				intf = line_parse[1] + line_parse[2]    	  #local interfaces for the device
				neighbour = line_parse[0] 					  #neighbours for the device
				portid = line_parse[-2] + line_parse[-1]      #neighbours' ports
				
				temp_list_keys.append(intf)               
				keys = tuple(temp_list_keys) 				  #dict key - tuple
				temp_list_values.append(neighbour) 				
				temp_list_values.append(portid)               
				values = tuple(temp_list_values)  			   #dict value - tuple
				
				final_dict[keys] = values
		return final_dict

				
print (parse_cdp_neighbors('sh_cdp_n_sw1.txt')) """

