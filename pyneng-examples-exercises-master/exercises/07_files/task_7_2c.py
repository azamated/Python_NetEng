# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import sys
file_raw = sys.argv[1]
file_cleared = sys.argv[2]

ignore = ['duplex', 'alias', 'Current configuration']

with open(file_raw, 'r') as f:
	for line in f:
		if ignore[0] in line:
			pass
		elif ignore[1] in line:
			pass
		elif ignore[2] in line:
			pass
		else:
			output = open(file_cleared, 'a')
			output.write(line)
			output.close()
