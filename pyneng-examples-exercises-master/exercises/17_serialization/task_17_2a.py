# -*- coding: utf-8 -*-
'''
Задание 17.2a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.

'''
from pprint import pprint
import yaml
from task_17_2 import parse_sh_cdp_neighbors

final_dict = {}

def generate_topology_from_cdp(list_of_files, save_to_filename = None):
	for item in list_of_files:
		with open(item) as f:
			data = f.read().replace('\n', '')
			temp_dict = parse_sh_cdp_neighbors(data)
			for key in temp_dict:
				final_dict[key] = temp_dict[key]
	if save_to_filename != None:
		with open(save_to_filename, "w+") as f:
			f = yaml.dump(final_dict, f)
		return
	else:
		return final_dict

if __name__ == "__main__":
	fileList = ('sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt', 'sh_cdp_n_r4.txt', 'sh_cdp_n_r5.txt', 'sh_cdp_n_r6.txt')
	fileSave = input("Enter a name of the output yaml file or hit enter to pass: ")
	
	if len(fileSave) == 0:
		pprint (generate_topology_from_cdp(fileList))
	else:
		pprint (generate_topology_from_cdp(fileList, fileSave))
	

