# -*- coding: utf-8 -*-
'''
Задание 5.1b

Переделать скрипт из задания 5.1a таким образом, чтобы, при запросе параметра,
отображался список возможных параметров. Список параметров надо получить из словаря,
а не прописывать вручную.

Вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:
$ python task_5_1b.py
Введите имя устройства: r1
Введите имя параметра (ios, model, vendor, location, ip): ip
10.255.0.1

Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if.
'''

london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
device_n = input('Введите имя устройства: ')
#device_p = 


list_items = list(london_co.items())
list_keys = list_items[0].keys()

print(list_items)
#print(list_keys)

#device_p = input('Введите имя параметра (ios, model, vendor, location, ip): ')
#print (london_co[device_n][device_p])
