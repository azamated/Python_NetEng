# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'
parse = mac.split(":")
binA = bin(int(parse[0], 16))
binB = bin(int(parse[0], 16))
binC = bin(int(parse[0], 16))

result = str(binA) + str(binB) + str(binC)
print(parse)
