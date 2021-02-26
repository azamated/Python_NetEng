# -*- coding: utf-8 -*-

import sqlite3
import os
import sys
from pprint import pprint
import yaml
import re

#Declaring global variables
dhcp_snooping_file_list = []
yaml_dict = {}
parsed_result = []
equipment_name = []

################################
###Add data to switches table#
################################

def add_data_switches(db_name, sw_file):
	temp_dict1 = yaml_converter(sw_file)
	for key, value in temp_dict1.items():
		temp_dict2 = value
	
	conn = sqlite3.connect(db_name)
	temp_list = []
	
	print('Inserting data into SWITCHES')
	for key, value in temp_dict2.items():
		query1 = 'INSERT into switches (hostname, location) values (?, ?)'
		temp_list= [key, value]
		print (temp_list)
		try:
			conn.execute(query1, temp_list)
			conn.commit()
			print ("success!")
		except sqlite3.IntegrityError as e:
			print ("Data already inserted")
	conn.close()

#Yaml converter
def yaml_converter(file_input):
	with open(file_input, 'r', encoding='UTF-8') as f:
		yaml_dict = yaml.safe_load(f)
	return yaml_dict

################################
###Add data to dhcp table#
################################

def add_data_dhcp(db_name, dhcp_files_list):
	for item in dhcp_files_list:
		row_data = txt_parser(item)
		#pprint (row_data)
		conn = sqlite3.connect(db_name)
	
		print('Inserting DHCP Snooping data')
		for row in row_data:
			pprint (row)
			query2 = 'INSERT into dhcp (mac, ip, vlan, interface, switch) values (?, ?, ?, ?, ?)'
			try:
				conn.execute(query2, row)
				conn.commit()
				print ("Success!!")
			except sqlite3.IntegrityError as e:
				print ("Data already inserted")
		conn.close()

#Find dhcp snooping files 
def dhcp_snooping_files():
	for item in os.listdir():
		if item.endswith('dhcp_snooping.txt'):
			dhcp_snooping_file_list.append(item)
	return dhcp_snooping_file_list


#Txt Parser, parses in to list of tuples
def txt_parser(input_data):
	parsed_result = []
	match1 = re.search(r'^(\S+)_dhcp', input_data)
	if match1:
		regex = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
		with open(input_data) as data:
			for line in data:
				match2 = regex.search(line)
				if match2:
					temp_list = list(match2.groups())
					temp_list.append(match1.group(1))
					temp_tuple = tuple(temp_list)
					parsed_result.append(temp_tuple)
			#print (parsed_result)
			return parsed_result

###########
#Main code#
###########

if __name__ == '__main__':
	if check_db(r"dhcp_snooping.db") == True:
		add_data_switches('dhcp_snooping.db','switches.yml')
		dhcp_snooping_files()
		add_data_dhcp('dhcp_snooping.db', dhcp_snooping_file_list)
	else:
		print ("Please create a DB first!")

#Checking if DB exists
def check_db(db_name):
	if os.path.isfile(db_name):
		print ("DB is created")
		db_flag = True
		return True
	else:
		return False	
	
	
	
	
	
