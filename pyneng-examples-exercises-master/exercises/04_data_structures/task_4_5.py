# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
split1 = command1.split()
split2 = command2.split()
parse1 = split1[-1].split(',')
parse2 = split2[-1].split(',')
parse1.extend(parse2)
result = sorted(set(parse1))
print (result)





