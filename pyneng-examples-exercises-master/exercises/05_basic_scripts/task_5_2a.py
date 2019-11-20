# -*- coding: utf-8 -*-
'''
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip_param= input("Please enter IP address with mask in the follwowing format: 10.1.1.0/24: ")
ip_param_parsed = ip_param.split("/") 
ip_add = ip_param_parsed[0].split(".")
                                                               
oct1 = int(ip_add[0])
oct2 = int(ip_add[1])
oct3 = int(ip_add[2])
oct4 = int(ip_add[3])
##################################################
maskint = int(ip_param_parsed[1])
maskbit = "1" * maskint ## string multiplied by numbers returns multiple strings
maskbit = "{:<032}".format(maskbit)
m1 = int(maskbit[0:8], 2) ###воспринимай однерки как двоичное число, но общее число десятичное, так как есть INT
m2 = int(maskbit[8:16], 2) 
m3 = int(maskbit[16:24], 2) 
m4 = int(maskbit[24:32], 2) 

ip1 = int(bin(oct1 & m1), 2)
ip2 = int(bin(oct2 & m2), 2)
ip3 = int(bin(oct3 & m3), 2)
ip4 = int(bin(oct4 & m4), 2)

print (ip1)

                                       
ip_template = """
IP
{:<10} {:<10} {:<10} {:<10}
{:010b} {:010b} {:010b} {:010b}"""
print (ip_template.format(ip1, ip2, ip3, ip4, ip1, ip2, ip3, ip4))

mask_template = """
Mask:
/{}
{:<10} {:<10} {:<10} {:<10}
{:010b} {:010b} {:010b} {:010b}"""
print (mask_template.format(maskint, m1, m2, m3, m4, m1, m2, m3, m4))
