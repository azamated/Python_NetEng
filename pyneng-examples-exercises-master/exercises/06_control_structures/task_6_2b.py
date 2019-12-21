# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip_correct = False
while not ip_correct:
	try:
		ip = input("Please enter IP address: ")
		ip_parsed = ip.split(".")
		if len(ip_parsed) == 4:
			octet_count = 0
			for octet in ip_parsed:
				octet_int = int(octet)
				if octet_int in range(0,256):
					octet_count += 1
					if octet_count == 4:
						ip_range = {	
								'A':[1, 127],
								'B':[128, 191],	
								'C':[192, 223],			
								'D':[224, 239],
								'255':[255, 255],
								'0':[0, 0],
							   }
								  
						ip_packet= {	
								'A':'unicast',
								'B':'unicast',			
								'C':'unicast',			
								'D':'multicast',
							  '255':'local broadcast',
								'0':'unassigned',
							   None: "unused"
							   }
						for item in ip_range:
							if int(ip_range[item][0]) <= int(ip_parsed[0]) <= int(ip_range[item][1]):
								network_class = item
								break
							else:
								network_class = None
						for key, value in ip_packet.items():
							if key== network_class:
								print(value)
								ip_correct = True
							
				else:
					print ("Please enter a correct IP addess")
					break
					ip_correct = False
		else:
			print ("Please enter a correct IP addess")
			ip_correct = False	

	except (ValueError, NameError):
		print ("Please enter a correct IP addess")
		ip_correct = False
