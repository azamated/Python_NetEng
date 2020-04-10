# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(config_filename):
	access_dic = {}
	trunk_dic = {}
	with open(config_filename) as f:
		for line in f:
			if line.startswith('interface'):
				interface = line.split()[1]
			elif line.startswith(' switchport access vlan'):
				vlan = int(line.split()[-1])
				access_dic[interface] = vlan
			elif line.startswith(' switchport mode access'):
				access_dic[interface] = 1
			elif line.startswith(' switchport trunk allowed vlan'):
				vlan = line.split()[-1]
				vlan_parsed = vlan.split(',')
				vlan_digits = []
				for item in vlan_parsed:
					item = int(item)
					vlan_digits.append(item)
					trunk_dic[interface] = vlan_digits
		return access_dic, trunk_dic
print (get_int_vlan_map('config_sw2.txt'))



