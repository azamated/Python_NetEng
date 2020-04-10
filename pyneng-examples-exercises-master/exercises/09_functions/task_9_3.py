# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


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
            elif line.startswith(' switchport trunk allowed vlan'):
                vlan = line.split()[-1]
                vlan_parsed = vlan.split(',')
                vlan_digits = []
                for item in vlan_parsed:
                    item = int(item)
                    vlan_digits.append(item)
                    trunk_dic[interface] = vlan_digits
        return access_dic, trunk_dic
print (get_int_vlan_map('config_sw1.txt'))
