# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
template = '''
{:<9}{:<20}{:<12}{:<6}
'''

list1 = []
with open('CAM_table.txt', 'r') as f: 
	str_file = f.read().rstrip().split('\n')
	for line in str_file :
		if "." in line:
			list1.append(line)
			
list2 = []
for item in list1:
	list_parsed = item.strip().split()
	list_temp = [int(list_parsed[0]), list_parsed[1], list_parsed[2], list_parsed[3]]
	list2.append(list_temp)
	list2.sort()

vlan_name = input('Enter Vlan number: ')
vlan_name = int(vlan_name)

for item in list2:
	if item[0]== vlan_name:
		print(template.format(item[0],item[1],item[2],item[3]), end='')
