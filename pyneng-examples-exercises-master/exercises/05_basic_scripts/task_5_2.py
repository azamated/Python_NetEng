# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

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

m1 = int(maskbit[0:8], 2) ###воспринимай однерки как двоичное число, но одщее число десятичное, так как есть INT
print (m1)
m2 = int(maskbit[8:16], 2) 
m3 = int(maskbit[16:24], 2) 
m4 = int(maskbit[24:32], 2) 

                                                        
ip_template = """
IP
{:<10} {:<10} {:<10} {:<10}
{:010b} {:010b} {:010b} {:010b}"""
print (ip_template.format(oct1, oct2, oct3, oct4, oct1, oct2, oct3, oct4))

mask_template = """
Mask:
/{}
{:<10} {:<10} {:<10} {:<10}
{:010b} {:010b} {:010b} {:010b}"""
print (mask_template.format(maskint, m1, m2, m3, m4, m1, m2, m3, m4))
