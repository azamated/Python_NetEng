# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9


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
	list_parsed = item.split()
	list_temp = [int(list_parsed[0]), list_parsed[1], list_parsed[2], list_parsed[3]]
	list2.append(list_temp)
	list2.sort()

for item in list2:
	print(template.format(item[0],item[1],item[2],item[3]), end='')


		




	

          
