# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
template = '''{:<9}{:<20}{:<12}{:<6}
'''

list1 = []
with open('CAM_table.txt', 'r') as f: 
	str_file = f.read().split('\n')
	for line in str_file :
		if "." in line:
			line = line.split()
			line[0] = int(line[0])
			list1.append(line)
			list1.sort()


vlan_name = input('Enter Vlan number: ')
vlan_name = int(vlan_name)

for item in list1:
	if item[0]== vlan_name:
		print(template.format(item[0],item[1],item[2],item[3]), end='')
