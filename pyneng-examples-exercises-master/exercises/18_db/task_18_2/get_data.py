# -*- coding: utf-8 -*-

import sqlite3
import os
import sys

#Declaring global variables
db_name = 'dhcp_snooping.db'
arg_list = []

#Check parameters entered by users
try:
	arg_list = sys.argv[1:]
except ValueError:
	print ("Script supports only none or two arguments!")

#Check if DB exists
def check_db(db_name):
	if os.path.isfile(db_name):
		print ("DB is created")
		db_flag = True
		return True
	else:
		return False	

#Check arguments
def check_args():
	if len(sys.argv) == 3:
		return True
	
	elif len(sys.argv) == 1:
		return True
	else:
		return False
	
#Get data from DB
def get_data(*args):
	if len(arg_list) == 2:
		conn = sqlite3.connect(db_name)
		query1 = 'select * from dhcp where {} = ?'.format(arg_list[0])
		result = conn.execute(query1, (arg_list[1], ))
	elif len(arg_list) == 0:
		conn = sqlite3.connect(db_name)
		result = conn.execute('select * from dhcp')
	for row in result:
		print (row)
	conn.close()
	
#Main code
if __name__ == '__main__':
	if check_db(db_name) == True:
		if check_args() == True:
			get_data()
		else: print ("Script supports only none or two arguments!")
	else:
		print ("A Database does not exist")
		
		
		
		
		
		
