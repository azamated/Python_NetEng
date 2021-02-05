# -*- coding: utf-8 -*-
'''
Задание 17.2b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).

Проверить работу функции на файле topology.yaml. На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.

Результат должен выглядеть так же, как схема в файле task_17_2b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''

from pprint import pprint
import yaml
from draw_network_graph import draw_topology

dict_topology = {}
final_dict = {}
tuple_key = ()
tuple_value = ()

#Funtions transforms a yaml file to graphic diagram
def transform_topology(inputYamlFile):
	with open(inputYamlFile) as f:
		dict_topology = yaml.safe_load(f)
		#pprint (dict_topology)
		
		for key, value in dict_topology.items():
			#print (value)
			
			for sub_key1, sub_value1 in value.items():
				tuple_key = (key, sub_key1)
				#print (tuple_key)
				
				for sub_key2, sub_value2 in sub_value1.items():
					tuple_value = (sub_key2, sub_value2)
					
					if tuple_key not in final_dict.values():
						#print (tuple_value)
						final_dict[tuple_key] = tuple_value
	 
	#pprint (final_dict)
	draw_topology(final_dict)
	return final_dict

if __name__ == "__main__":
	input_yaml_file = 'topology.yaml'
	transform_topology(input_yaml_file)
	
	
	
		
